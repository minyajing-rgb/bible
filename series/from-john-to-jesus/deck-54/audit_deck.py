#!/usr/bin/env python3
"""Fail fast when deck structure or two-pass source verification is incomplete."""

import json
from pathlib import Path

from PIL import Image

from render_spades_mark import MARK_CARDS


ROOT = Path(__file__).resolve().parent
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["SPADES", "DIAMONDS", "CLUBS", "HEARTS"]
ALLOWED_QUOTES = {"NARRATION", "DIRECT_JESUS", "DIRECT_JOHN_BAPTIST", "DIRECT_OTHER"}


def fail(message: str) -> None:
    raise SystemExit(f"DECK AUDIT FAILED: {message}")


ledger = json.loads((ROOT / "ledger.json").read_text())
cards = ledger["cards"]
if len(cards) != 54:
    fail(f"expected 54 ledger cards, found {len(cards)}")

ids = [card["id"] for card in cards]
if len(ids) != len(set(ids)):
    fail("duplicate card IDs")

for suit in SUITS:
    ranks = [card["rank"] for card in cards if card.get("suit") == suit]
    if ranks != RANKS:
        fail(f"{suit} must contain A–K in order; found {ranks}")

audit = json.loads((ROOT / "audit" / "verified-cards.json").read_text())
verified = {card["id"]: card for card in audit["cards"]}
for card_id, record in verified.items():
    if card_id not in ids:
        fail(f"verification record {card_id} is absent from ledger")
    for field in ("quote_verse", "greek", "literal_english", "speaker", "quote_type", "historical_status"):
        if not record.get(field):
            fail(f"{card_id} is missing {field}")
    if record["quote_type"] not in ALLOWED_QUOTES:
        fail(f"{card_id} has invalid quote type {record['quote_type']}")
    if record.get("pass_1") != "PASS" or record.get("pass_2") != "PASS":
        fail(f"{card_id} has not passed both source checks")
    ledger_card = next(card for card in cards if card["id"] == card_id)
    if ledger_card["source"] != record["quote_verse"]:
        fail(f"{card_id} ledger source {ledger_card['source']} != audited unit {record['quote_verse']}")
    if ledger_card["speaker"] != record["speaker"]:
        fail(f"{card_id} ledger speaker does not match audited speaker")
    if ledger_card["quote_type"] != record["quote_type"]:
        fail(f"{card_id} ledger quote type does not match audited quote type")

# Every currently rendered suited proof must already have a two-pass record.
rendered_map = {
    "ace-spades-mark.png": "SP-A",
    "ace-diamonds-matthew.png": "DI-A",
    "ace-clubs-luke.png": "CL-A",
    "ace-hearts-john.png": "HE-A",
}
for filename, card_id in rendered_map.items():
    if (ROOT / "final" / filename).exists() and card_id not in verified:
        fail(f"rendered card {filename} lacks two-pass verification")

# Every rendered production asset is delivered as a matched bleed/trim pair.
rendered_assets = [
    "joker-big-love-light.png",
    "joker-small-jesus-heart.png",
    *rendered_map.keys(),
    "card-back.png",
]
for filename in rendered_assets:
    print_path = ROOT / "print" / filename
    final_path = ROOT / "final" / filename
    if not print_path.exists() or not final_path.exists():
        fail(f"{filename} is missing its print/final pair")
    if Image.open(print_path).size != (815, 1110):
        fail(f"{filename} print file is not 815×1110")
    if Image.open(final_path).size != (745, 1040):
        fail(f"{filename} trimmed file is not 745×1040")

mark_ids = [f"SP-{rank}" for rank in RANKS]
missing_mark = [card_id for card_id in mark_ids if card_id not in verified]
if missing_mark:
    fail(f"Mark A–K second pass incomplete: {missing_mark}")

rendered_mark = {card["id"]: card for card in MARK_CARDS}
for card_id in mark_ids:
    record = verified[card_id]
    rendered = rendered_mark.get(card_id)
    if not rendered:
        fail(f"{card_id} is absent from the Mark renderer")
    if rendered["source"] != record["quote_verse"]:
        fail(f"{card_id} rendered source does not match audit")
    if rendered["quote"] != record.get("display_quote"):
        fail(f"{card_id} rendered display quote does not match audit")
    for folder, size in (("print", (815, 1110)), ("final", (745, 1040))):
        filename = rendered["output"]
        path = ROOT / folder / filename
        if not path.exists() or Image.open(path).size != size:
            fail(f"{card_id} is missing a valid {folder} render")

packaging_expected = {
    ROOT / "packaging" / "print" / "tuck-box-artwork.png": (2220, 1723),
    ROOT / "packaging" / "proof" / "tuck-box-dieline-proof.png": (2220, 1723),
    ROOT / "packaging" / "final" / "tuck-box-front.png": (768, 1063),
    ROOT / "packaging" / "final" / "tuck-box-back.png": (768, 1063),
}
for path, size in packaging_expected.items():
    if not path.exists() or Image.open(path).size != size:
        fail(f"packaging asset {path.name} is missing or has the wrong size")

print(
    f"DECK AUDIT PASSED: 54 cards; {len(verified)} source records verified; "
    "Mark A–K rendered; packaging proof complete"
)
