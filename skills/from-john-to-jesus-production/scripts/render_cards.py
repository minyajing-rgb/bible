#!/usr/bin/env python3
"""Render exact, reference-style typography over approved no-text illustrations."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
INK = "#292927"
MUTED = "#66645f"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(SANS, size=size)


def wrap(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=face)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, face: ImageFont.FreeTypeFont,
             fill: str, width: int) -> int:
    box = draw.textbbox((0, 0), text, font=face)
    x = (width - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=face, fill=fill)
    return y + (box[3] - box[1])


def centered_wrapped(draw: ImageDraw.ImageDraw, y: int, text: str, face: ImageFont.FreeTypeFont,
                     fill: str, width: int, max_width: int, spacing: int) -> int:
    for line in wrap(draw, text, face, max_width):
        centered(draw, y, line, face, fill, width)
        y += spacing
    return y


def spaced_text(draw: ImageDraw.ImageDraw, y: int, text: str, face: ImageFont.FreeTypeFont,
                fill: str, width: int, tracking: int) -> int:
    glyphs = [draw.textlength(ch, font=face) for ch in text]
    total = sum(glyphs) + tracking * max(0, len(text) - 1)
    x = (width - total) / 2
    for ch, glyph_width in zip(text, glyphs):
        draw.text((x, y), ch, font=face, fill=fill)
        x += glyph_width + tracking
    return y + face.size


def draw_leaf_mark(draw: ImageDraw.ImageDraw, width: int, y: int) -> None:
    x = width // 2
    draw.line((x, y + 24, x, y + 47), fill=INK, width=3)
    draw.ellipse((x - 9, y + 4, x + 6, y + 31), fill=INK)
    draw.arc((x - 24, y + 44, x, y + 56), 185, 350, fill=INK, width=2)
    draw.arc((x, y + 44, x + 24, y + 56), 190, 355, fill=INK, width=2)


def compose_scene(raw: Image.Image) -> Image.Image:
    """Move the generated no-text scene into a protected illustration zone.

    Image generation leaves a large blank field but does not place every scene at
    exactly the same vertical coordinate.  Extracting the ink and rebuilding the
    blank paper prevents captions and source notes from crossing the figures.
    """
    w, h = raw.size
    paper = raw.crop((0, 0, w, min(620, h))).resize((w, h), Image.Resampling.BICUBIC)

    gray = raw.convert("L")
    alpha = gray.point(lambda value: max(0, min(255, (235 - value) * 4)))
    bbox = alpha.point(lambda value: 255 if value > 20 else 0).getbbox()
    if not bbox:
        return paper

    left, top, right, bottom = bbox
    pad = 14
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(w, right + pad)
    bottom = min(h, bottom + pad)
    scene = raw.crop((left, top, right, bottom))
    scene_alpha = alpha.crop((left, top, right, bottom))

    max_width = int(w * 0.91)
    max_height = int(h * 0.19)
    scale = min(max_width / scene.width, max_height / scene.height, 1.0)
    size = (max(1, int(scene.width * scale)), max(1, int(scene.height * scale)))
    scene = scene.resize(size, Image.Resampling.LANCZOS)
    scene_alpha = scene_alpha.resize(size, Image.Resampling.LANCZOS)
    x = (w - size[0]) // 2
    y = int(h * 0.465)
    paper.paste(scene, (x, y), scene_alpha)
    return paper


def render_card(batch_dir: Path, item: dict) -> None:
    raw = compose_scene(Image.open(batch_dir / item["raw_file"]).convert("RGB"))
    overlay = Image.new("RGBA", raw.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = raw.size

    spaced_text(
        draw,
        int(h * 0.055),
        "GGC Spirituality Series · From John to Jesus",
        font(max(13, int(w * 0.017))),
        INK,
        w,
        max(2, int(w * 0.003)),
    )

    centered(draw, int(h * 0.135), "LITERAL ENGLISH", font(max(11, int(w * 0.013))), MUTED, w)

    quote_face = font(max(28, int(w * 0.041)))
    quote_y = int(h * 0.17)
    quote_y = centered_wrapped(
        draw,
        quote_y,
        f'“{item["exact_quote"]}”',
        quote_face,
        INK,
        w,
        int(w * 0.80),
        int(quote_face.size * 1.42),
    )

    verse_y = quote_y + int(h * 0.012)
    centered(draw, verse_y, f'{item["source_book"]} {item["source_verse"]}', font(max(15, int(w * 0.019))), INK, w)
    greek_label_y = verse_y + int(h * 0.032)
    centered(draw, greek_label_y, "EARLIEST RECOVERABLE GREEK", font(max(11, int(w * 0.013))), MUTED, w)
    greek_y = greek_label_y + int(h * 0.028)
    centered_wrapped(draw, greek_y, item["greek"], font(max(13, int(w * 0.016))), MUTED, w, int(w * 0.78), 27)

    caption_y = int(h * 0.675)
    spaced_text(draw, caption_y, item["caption"], font(max(13, int(w * 0.016))), INK, w, 2)

    meta_face = font(max(12, int(w * 0.014)))
    meta_y = int(h * 0.72)
    metadata = [
        f'SOURCE: {item["source_book"]} {item["source_verse"]}',
        f'SOURCE LAYER: {item["source_layer"].upper()}',
        f'DATE: {item["date"]}',
        f'PARALLEL: {item["parallel"]}',
        f'HISTORICAL STATUS: {item["historical_status"]}',
        f'{item["note_label"]}: {item["note"]}',
    ]
    for line in metadata:
        meta_y = centered_wrapped(draw, meta_y, line, meta_face, MUTED, w, int(w * 0.86), 20)
        meta_y += 8

    mark_y = int(h * 0.93)
    draw_leaf_mark(draw, w, mark_y)
    spaced_text(draw, int(h * 0.965), "GGC Spirituality Series", font(max(11, int(w * 0.014))), INK, w, 3)

    final = Image.alpha_composite(raw.convert("RGBA"), overlay).convert("RGB")
    out = batch_dir / item["final_file"]
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = out.with_suffix(".tmp.ppm")
    final.save(temporary, "PPM")
    for attempt in range(3):
        out.unlink(missing_ok=True)
        subprocess.run(
            ["convert", str(temporary), "-strip", "-colors", "64", f"PNG8:{out}"],
            check=True,
        )
        try:
            with Image.open(out) as check:
                check.load()
            break
        except OSError:
            if attempt == 2:
                raise
    temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_dir", type=Path)
    args = parser.parse_args()
    ledger = json.loads((args.batch_dir / "ledger.json").read_text(encoding="utf-8"))
    if len(ledger) != 10:
        raise SystemExit(f"Expected exactly 10 ledger rows, found {len(ledger)}")
    for item in ledger:
        render_card(args.batch_dir, item)
    print(f"Rendered {len(ledger)} cards")


if __name__ == "__main__":
    main()
