#!/usr/bin/env python3
"""Audit one From John to Jesus batch before publication."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


REQUIRED = {
    "episode_id", "batch_id", "john_identity", "timeline_order", "source_book",
    "source_verse", "speaker", "quote_type", "exact_quote", "greek",
    "scene_action", "caption", "accent_color", "certainty", "source_layer", "date", "parallel",
    "historical_status", "note_label", "note", "critical_text_basis", "change_track",
    "raw_file", "final_file",
}


def dark_pixel_count(image: Image.Image, top: float, bottom: float) -> int:
    gray = image.convert("L")
    y0 = int(gray.height * top)
    y1 = int(gray.height * bottom)
    band = gray.crop((0, y0, gray.width, y1))
    return sum(1 for value in band.get_flattened_data() if value < 190)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_dir", type=Path)
    args = parser.parse_args()
    ledger = json.loads((args.batch_dir / "ledger.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    if len(ledger) != 10:
        errors.append(f"ledger has {len(ledger)} rows, expected 10")
    ids: set[str] = set()
    for idx, row in enumerate(ledger, start=1):
        missing = REQUIRED - row.keys()
        if missing:
            errors.append(f"row {idx} missing: {sorted(missing)}")
        if row.get("john_identity") != "JOHN_BAPTIST":
            errors.append(f"row {idx} has forbidden identity {row.get('john_identity')!r}")
        if row.get("episode_id") in ids:
            errors.append(f"duplicate episode_id {row.get('episode_id')}")
        ids.add(row.get("episode_id", ""))
        track = row.get("change_track", [])
        if not track:
            errors.append(f"row {idx} has no change_track entries")
        for event_index, event in enumerate(track, start=1):
            missing_event = {"date", "category", "witness", "statement", "certainty"} - event.keys()
            if missing_event:
                errors.append(f"row {idx} change_track {event_index} missing: {sorted(missing_event)}")
            if event.get("category") not in {"GOSPEL_REDACTION", "SCRIBAL_VARIANT", "TRANSLATION_HISTORY"}:
                errors.append(f"row {idx} change_track {event_index} has invalid category")
        for key in ("raw_file", "final_file"):
            path = args.batch_dir / row.get(key, "")
            if not path.is_file():
                errors.append(f"row {idx} missing {key}: {path}")
                continue
            try:
                with Image.open(path) as image:
                    image.load()
                    ratio = image.width / image.height
                    if not 0.78 <= ratio <= 0.82:
                        errors.append(f"row {idx} {key} is not approximately 4:5: {image.size}")
                    if key == "final_file":
                        checks = {
                            "brand header": (0.03, 0.11, 150),
                            "Greek and literal text zone": (0.10, 0.38, 700),
                            "version history zone": (0.67, 0.93, 850),
                        }
                        for label, (top, bottom, minimum) in checks.items():
                            if dark_pixel_count(image, top, bottom) < minimum:
                                errors.append(f"row {idx} final_file lacks visible {label}")
            except Exception as exc:
                errors.append(f"row {idx} unreadable {key}: {exc}")
    if errors:
        raise SystemExit("AUDIT FAILED\n- " + "\n- ".join(errors))
    print(f"AUDIT PASSED: {len(ledger)} cards, JOHN_BAPTIST identity locked, files readable")


if __name__ == "__main__":
    main()
