#!/usr/bin/env python3
"""Render the four Gospel Aces and the common two-way card back."""

from __future__ import annotations

import math
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
FINAL = ROOT / "final"
PRINT = ROOT / "print"
PROOF = ROOT / "proof"

CARD = (815, 1110)
BLEED = 35
TRIM = (CARD[0] - BLEED * 2, CARD[1] - BLEED * 2)
BG = (250, 249, 246)
INK = (35, 34, 32)
MUTED = (99, 95, 89)
SKY = (104, 163, 190)
GOLD = (190, 142, 47)
SAGE = (126, 158, 116)
CORAL = (221, 116, 91)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


CARDS = [
    {
        "id": "SP-A",
        "rank": "A",
        "suit": "♠",
        "gospel": "MARK",
        "raw": "ace-spades-mark.png",
        "output": "ace-spades-mark.png",
        "title": "A VOICE IN THE WILDERNESS",
        "quote": "Prepare the way of the Lord.",
        "source": "Mark 1:3",
        "layer": "EARLIEST EXTANT GOSPEL OPENING",
        "date": "c. 65–75 CE",
        "accent": SKY,
    },
    {
        "id": "DI-A",
        "rank": "A",
        "suit": "♦",
        "gospel": "MATTHEW",
        "raw": "ace-diamonds-matthew.png",
        "output": "ace-diamonds-matthew.png",
        "title": "THE KINGDOM HAS DRAWN NEAR",
        "quote": "Repent, for the kingdom of heaven has drawn near.",
        "source": "Matthew 3:2",
        "layer": "MATTHEAN OPENING",
        "date": "c. 80–95 CE",
        "accent": GOLD,
    },
    {
        "id": "CL-A",
        "rank": "A",
        "suit": "♣",
        "gospel": "LUKE",
        "raw": "ace-clubs-luke.png",
        "output": "ace-clubs-luke.png",
        "title": "A BIRTH IS ANNOUNCED",
        "quote": "Your wife Elizabeth will bear you a son.",
        "source": "Luke 1:13",
        "layer": "LUKE-ONLY INFANCY TRADITION",
        "date": "c. 80–95 CE",
        "accent": SAGE,
    },
    {
        "id": "HE-A",
        "rank": "A",
        "suit": "♥",
        "gospel": "JOHN",
        "raw": "ace-hearts-john.png",
        "output": "ace-hearts-john.png",
        "title": "WITNESS TO THE LIGHT",
        "quote": "He was not the light, but came to testify about the light.",
        "source": "John 1:8",
        "layer": "JOHANNINE THEOLOGICAL FRAME",
        "date": "c. 90–100 CE",
        "accent": CORAL,
    },
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, fnt, fill=INK) -> None:
    draw.text(((CARD[0] - text_width(draw, text, fnt)) / 2, y), text, font=fnt, fill=fill)


def crop_art(path: Path) -> Image.Image:
    image = Image.open(path).convert("RGB")
    white = Image.new("RGB", image.size, "white")
    diff = ImageChops.difference(image, white).convert("L")
    diff = diff.point(lambda px: 255 if px > 14 else 0)
    box = diff.getbbox()
    if box is None:
        return image
    left, top, right, bottom = box
    pad_x = max(24, (right - left) // 18)
    pad_y = max(24, (bottom - top) // 18)
    return image.crop(
        (
            max(0, left - pad_x),
            max(0, top - pad_y),
            min(image.width, right + pad_x),
            min(image.height, bottom + pad_y),
        )
    )


def transparent_art(path: Path, size: tuple[int, int]) -> Image.Image:
    art = ImageOps.contain(crop_art(path), size, Image.Resampling.LANCZOS).convert("RGBA")
    pixels = art.load()
    for y in range(art.height):
        for x in range(art.width):
            r, g, b, _ = pixels[x, y]
            alpha = max(0, min(255, (255 - min(r, g, b)) * 12))
            pixels[x, y] = (r, g, b, alpha)
    return art


def corner(card: Image.Image, rank: str, suit: str, accent, flip: bool = False) -> None:
    layer = Image.new("RGBA", (132, 176), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((19, 7), rank, font=font(45, True), fill=INK)
    d.text((17, 57), suit, font=font(36), fill=accent)
    if flip:
        layer = layer.rotate(180)
        card.alpha_composite(layer, (CARD[0] - layer.width - 54, CARD[1] - layer.height - 50))
    else:
        card.alpha_composite(layer, (54, 50))


def save_print_and_trim(card: Image.Image, filename: str, colors: int = 256) -> Path:
    """Save the bleed canvas and the centered trim-size production file."""
    PRINT.mkdir(parents=True, exist_ok=True)
    FINAL.mkdir(parents=True, exist_ok=True)
    print_output = PRINT / filename
    final_output = FINAL / filename
    print_tmp = print_output.with_name(f".{print_output.name}.tmp")
    final_tmp = final_output.with_name(f".{final_output.name}.tmp")
    rgb = card.convert("RGB")
    rgb.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(
        print_tmp, format="PNG", optimize=False, compress_level=6, dpi=(300, 300)
    )
    rgb.crop((BLEED, BLEED, CARD[0] - BLEED, CARD[1] - BLEED)).quantize(
        colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE
    ).save(final_tmp, format="PNG", optimize=False, compress_level=6, dpi=(300, 300))
    print_tmp.replace(print_output)
    final_tmp.replace(final_output)
    return final_output


def render_front(data: dict) -> Path:
    card = Image.new("RGBA", CARD, BG + (255,))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        (BLEED + 10, BLEED + 10, CARD[0] - BLEED - 10, CARD[1] - BLEED - 10),
        radius=28,
        outline=(91, 88, 82),
        width=2,
    )
    corner(card, data.get("rank", "A"), data["suit"], data["accent"])
    corner(card, data.get("rank", "A"), data["suit"], data["accent"], flip=True)

    centered(draw, 83, "GGC SPIRITUALITY SERIES", font(14), MUTED)
    centered(draw, 112, "FROM JOHN TO JESUS", font(15, True), INK)
    centered(draw, 147, data["gospel"], font(16, True), data["accent"])

    art = transparent_art(RAW / data["raw"], (660, 565))
    card.alpha_composite(art, ((CARD[0] - art.width) // 2, 194 + (565 - art.height) // 2))

    centered(draw, 781, data["title"], font(25, True), INK)
    quote_lines = wrap(data["quote"], width=53)
    quote_y = 827
    for line in quote_lines[:2]:
        centered(draw, quote_y, line, font(17), INK)
        quote_y += 27
    centered(draw, 890, f'{data["source"]}  ·  {data["date"]}', font(15, True), data["accent"])

    badge_text = data["layer"]
    badge_font = font(12 if len(badge_text) < 33 else 10, True)
    badge_w = text_width(draw, badge_text, badge_font) + 34
    draw.rounded_rectangle(
        ((CARD[0] - badge_w) / 2, 930, (CARD[0] + badge_w) / 2, 963),
        radius=16,
        fill=data["accent"] + (35,),
        outline=data["accent"],
        width=1,
    )
    centered(draw, 939, badge_text, badge_font, INK)
    centered(draw, 985, f'Archive ID {data["id"]} · full Greek and transmission record online', font(11), MUTED)

    return save_print_and_trim(card, data["output"])


def heart_points(cx: float, cy: float, scale: float, rotate: bool = False) -> list[tuple[float, float]]:
    points = []
    for i in range(181):
        t = 2 * math.pi * i / 180
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        px = cx + x * scale
        py = cy - y * scale
        if rotate:
            px, py = 2 * cx - px, 2 * cy - py
        points.append((px, py))
    return points


def render_back() -> Path:
    card = Image.new("RGB", CARD, BG)
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        (BLEED + 10, BLEED + 10, CARD[0] - BLEED - 10, CARD[1] - BLEED - 10),
        radius=28,
        outline=INK,
        width=2,
    )
    draw.rounded_rectangle(
        (BLEED + 30, BLEED + 30, CARD[0] - BLEED - 30, CARD[1] - BLEED - 30),
        radius=22,
        outline=GOLD,
        width=3,
    )

    # Rotationally symmetric corner field; there is no top/bottom clue.
    inset = BLEED + 64
    for x, y in [(inset, inset), (CARD[0] - inset, inset), (inset, CARD[1] - inset), (CARD[0] - inset, CARD[1] - inset)]:
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=GOLD)
        draw.ellipse((x - 20, y - 20, x + 20, y + 20), outline=INK, width=2)

    cx, cy = CARD[0] / 2, CARD[1] / 2
    sun_radius = 132
    draw.ellipse(
        (cx - sun_radius, cy - sun_radius, cx + sun_radius, cy + sun_radius),
        fill=(248, 239, 207),
        outline=INK,
        width=3,
    )
    draw.ellipse((cx - 108, cy - 108, cx + 108, cy + 108), outline=GOLD, width=4)
    for angle in range(0, 360, 15):
        a = math.radians(angle)
        r1 = 154
        r2 = 208 if angle % 30 == 0 else 184
        draw.line(
            (cx + math.cos(a) * r1, cy + math.sin(a) * r1, cx + math.cos(a) * r2, cy + math.sin(a) * r2),
            fill=GOLD if angle % 30 == 0 else INK,
            width=4 if angle % 30 == 0 else 2,
        )

    # Two pointed hearts meet and overlap slightly at their tips inside the sun.
    draw.line(heart_points(cx, cy - 37, 3.15), fill=INK, width=4, joint="curve")
    draw.line(heart_points(cx, cy + 37, 3.15, rotate=True), fill=INK, width=4, joint="curve")
    draw.ellipse((cx - 7, cy - 7, cx + 7, cy + 7), fill=GOLD)

    return save_print_and_trim(card, "card-back.png", colors=128)


def contact_sheet(paths: list[Path], name: str, columns: int = 3) -> None:
    thumb_w = 286
    thumb_h = round(TRIM[1] * thumb_w / TRIM[0])
    rows = math.ceil(len(paths) / columns)
    sheet = Image.new("RGB", (columns * thumb_w + (columns + 1) * 24, rows * thumb_h + (rows + 1) * 24), (235, 233, 228))
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 24 + (index % columns) * (thumb_w + 24)
        y = 24 + (index // columns) * (thumb_h + 24)
        sheet.paste(image, (x, y))
    PROOF.mkdir(parents=True, exist_ok=True)
    sheet.save(PROOF / name, quality=94)


if __name__ == "__main__":
    ace_paths = [render_front(data) for data in CARDS]
    back_path = render_back()
    contact_sheet(ace_paths + [back_path], "aces-and-back-contact-sheet.jpg")
    joker_paths = [FINAL / "joker-big-love-light.png", FINAL / "joker-small-jesus-heart.png"]
    contact_sheet(joker_paths + ace_paths + [back_path], "style-proof-7-contact-sheet.jpg", columns=4)
