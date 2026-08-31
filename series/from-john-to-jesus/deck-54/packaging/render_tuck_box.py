#!/usr/bin/env python3
"""Render a generic 54-card tuck-box artwork and review dieline at 300 dpi."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
PRINT = ROOT / "print"
FINAL = ROOT / "final"
PROOF = ROOT / "proof"

DPI = 300
PX_PER_MM = DPI / 25.4


def mm(value: float) -> int:
    return round(value * PX_PER_MM)


BLEED = mm(3)
GLUE = mm(12)
PANEL_W = mm(65)
SIDE_W = mm(20)
BODY_H = mm(90)
FLAP_H = mm(25)
CANVAS = (BLEED * 2 + GLUE + PANEL_W * 2 + SIDE_W * 2, BLEED * 2 + FLAP_H * 2 + BODY_H)

BG = (250, 249, 246)
INK = (35, 34, 32)
MUTED = (104, 99, 91)
GOLD = (190, 142, 47)
PALE_GOLD = (248, 239, 207)
CUT = (213, 76, 72)
FOLD = (75, 133, 173)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False):
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def centered(draw: ImageDraw.ImageDraw, box, y: int, text: str, fnt, fill=INK) -> None:
    left, _, right, _ = box
    bounds = draw.textbbox((0, 0), text, font=fnt)
    width = bounds[2] - bounds[0]
    draw.text((left + (right - left - width) / 2, y), text, font=fnt, fill=fill)


def heart_points(cx: float, cy: float, scale: float, rotate: bool = False):
    points = []
    for index in range(181):
        t = 2 * math.pi * index / 180
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        px, py = cx + x * scale, cy - y * scale
        if rotate:
            px, py = 2 * cx - px, 2 * cy - py
        points.append((px, py))
    return points


def sun(draw: ImageDraw.ImageDraw, cx: int, cy: int, radius: int) -> None:
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=PALE_GOLD, outline=INK, width=4)
    draw.ellipse((cx - radius * .78, cy - radius * .78, cx + radius * .78, cy + radius * .78), outline=GOLD, width=5)
    for angle in range(0, 360, 15):
        a = math.radians(angle)
        inner = radius * 1.18
        outer = radius * (1.55 if angle % 30 == 0 else 1.38)
        draw.line(
            (cx + math.cos(a) * inner, cy + math.sin(a) * inner, cx + math.cos(a) * outer, cy + math.sin(a) * outer),
            fill=GOLD if angle % 30 == 0 else INK,
            width=4 if angle % 30 == 0 else 2,
        )
    scale = radius / 42
    draw.line(heart_points(cx, cy - radius * .28, scale), fill=INK, width=4, joint="curve")
    draw.line(heart_points(cx, cy + radius * .28, scale, rotate=True), fill=INK, width=4, joint="curve")
    draw.ellipse((cx - 7, cy - 7, cx + 7, cy + 7), fill=GOLD)


def vertical_text(image: Image.Image, box, text: str) -> None:
    width = box[2] - box[0]
    height = box[3] - box[1]
    layer = Image.new("RGBA", (height, width), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    fnt = font(22, True)
    bounds = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((height - (bounds[2] - bounds[0])) / 2, (width - (bounds[3] - bounds[1])) / 2), text, font=fnt, fill=INK)
    rotated = layer.rotate(90, expand=True)
    image.alpha_composite(rotated, (box[0], box[1]))


def panel_boxes():
    x0 = BLEED
    x1 = x0 + GLUE
    x2 = x1 + PANEL_W
    x3 = x2 + SIDE_W
    x4 = x3 + PANEL_W
    x5 = x4 + SIDE_W
    y0 = BLEED
    y1 = y0 + FLAP_H
    y2 = y1 + BODY_H
    y3 = y2 + FLAP_H
    return {
        "glue": (x0, y1, x1, y2),
        "back": (x1, y1, x2, y2),
        "side_left": (x2, y1, x3, y2),
        "front": (x3, y1, x4, y2),
        "side_right": (x4, y1, x5, y2),
        "top_back": (x1, y0, x2, y1),
        "top_front": (x3, y0, x4, y1),
        "bottom_back": (x1, y2, x2, y3),
        "bottom_front": (x3, y2, x4, y3),
        "bounds": (x0, y0, x5, y3),
    }


def render_artwork() -> Image.Image:
    image = Image.new("RGBA", CANVAS, BG + (255,))
    draw = ImageDraw.Draw(image)
    boxes = panel_boxes()

    for key in ("back", "front", "side_left", "side_right", "top_back", "top_front", "bottom_back", "bottom_front"):
        draw.rectangle(boxes[key], fill=BG, outline=(223, 217, 205), width=1)

    front = boxes["front"]
    fx = (front[0] + front[2]) // 2
    sun(draw, fx, front[1] + mm(31), mm(13))
    centered(draw, front, front[1] + mm(52), "GGC SPIRITUALITY SERIES", font(18), MUTED)
    centered(draw, front, front[1] + mm(59), "FROM JOHN TO JESUS", font(32, True), INK)
    centered(draw, front, front[1] + mm(68), "THE WITNESS · THE WATER · THE LIGHT", font(17, True), GOLD)
    centered(draw, front, front[1] + mm(77), "54-CARD GOSPEL DECK", font(18, True), INK)
    centered(draw, front, front[1] + mm(83), "EARLIEST RECOVERABLE GREEK · SOURCE-LAYERED", font(12), MUTED)

    back = boxes["back"]
    centered(draw, back, back[1] + mm(8), "FOUR GOSPELS · FOUR EDITORIAL LENSES", font(19, True), INK)
    centered(draw, back, back[1] + mm(17), "♠  MARK · EARLIEST EXTANT NARRATIVE SPINE", font(15, True), (89, 143, 169))
    centered(draw, back, back[1] + mm(24), "♦  MATTHEW · EXPLANATION & FULFILLMENT", font(15, True), GOLD)
    centered(draw, back, back[1] + mm(31), "♣  LUKE · ETHICS, PRAYER & RETURNED REPORT", font(15, True), (109, 143, 99))
    centered(draw, back, back[1] + mm(38), "♥  JOHN · WITNESS, LIGHT & REFRAMING", font(15, True), (197, 96, 76))
    centered(draw, back, back[1] + mm(51), "John means John the Baptist.", font(16, True), INK)
    centered(draw, back, back[1] + mm(58), "Each suited card records one exact text unit and speaker.", font(14), MUTED)
    centered(draw, back, back[1] + mm(64), "Gospel redaction, scribal variants, and later translation", font(14), MUTED)
    centered(draw, back, back[1] + mm(69), "are labeled separately. No surviving autograph is claimed.", font(14), MUTED)
    centered(draw, back, back[1] + mm(79), "bible.saga1001.com", font(19, True), GOLD)
    centered(draw, back, back[1] + mm(84), "TEXT HISTORY ARCHIVE", font(12, True), MUTED)

    vertical_text(image, boxes["side_left"], "FROM JOHN TO JESUS")
    vertical_text(image, boxes["side_right"], "THE WITNESS · THE WATER · THE LIGHT")

    top_front = boxes["top_front"]
    sun(draw, (top_front[0] + top_front[2]) // 2, (top_front[1] + top_front[3]) // 2, mm(5))
    centered(draw, boxes["bottom_front"], boxes["bottom_front"][1] + mm(10), "GGC SPIRITUALITY SERIES", font(17, True), INK)
    centered(draw, boxes["bottom_back"], boxes["bottom_back"][1] + mm(10), "54 CARDS · POKER SIZE", font(17, True), INK)
    return image


def render_dieline(artwork: Image.Image) -> Image.Image:
    proof = artwork.copy()
    draw = ImageDraw.Draw(proof)
    boxes = panel_boxes()
    cut_width = 3
    fold_width = 2
    # Generic review outline only; vendor dieline must replace this geometry.
    draw.rectangle(boxes["bounds"], outline=CUT, width=cut_width)
    x_lines = sorted({boxes[key][0] for key in ("back", "side_left", "front", "side_right")} | {boxes["side_right"][2]})
    for x in x_lines:
        draw.line((x, boxes["back"][1], x, boxes["back"][3]), fill=FOLD, width=fold_width)
    for y in (boxes["back"][1], boxes["back"][3]):
        draw.line((boxes["back"][0], y, boxes["side_right"][2], y), fill=FOLD, width=fold_width)
    draw.text((BLEED + 8, BLEED + 8), "PROOF ONLY · RED CUT / BLUE FOLD · REPLACE WITH PRINTER DIELINE", font=font(16, True), fill=CUT)
    return proof


if __name__ == "__main__":
    for folder in (PRINT, FINAL, PROOF):
        folder.mkdir(parents=True, exist_ok=True)
    artwork = render_artwork().convert("RGB")
    artwork.save(PRINT / "tuck-box-artwork.png", dpi=(DPI, DPI), optimize=True)
    render_dieline(artwork.convert("RGBA")).convert("RGB").save(
        PROOF / "tuck-box-dieline-proof.png", dpi=(DPI, DPI), optimize=True
    )
    boxes = panel_boxes()
    artwork.crop(boxes["front"]).save(FINAL / "tuck-box-front.png", dpi=(DPI, DPI), optimize=True)
    artwork.crop(boxes["back"]).save(FINAL / "tuck-box-back.png", dpi=(DPI, DPI), optimize=True)
    print(f"Rendered tuck-box proof at {CANVAS[0]}×{CANVAS[1]} px.")
