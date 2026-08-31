#!/usr/bin/env python3
"""Render the two symbolic Jokers into print-front proof cards."""

from pathlib import Path

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
GOLD = (190, 142, 47)
CORAL = (221, 116, 91)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def crop_art(path: Path) -> Image.Image:
    image = Image.open(path).convert("RGB")
    white = Image.new("RGB", image.size, "white")
    diff = ImageChops.difference(image, white).convert("L")
    diff = diff.point(lambda px: 255 if px > 16 else 0)
    box = diff.getbbox()
    if box is None:
        return image
    left, top, right, bottom = box
    pad_x = max(24, (right - left) // 12)
    pad_y = max(24, (bottom - top) // 12)
    box = (
        max(0, left - pad_x),
        max(0, top - pad_y),
        min(image.width, right + pad_x),
        min(image.height, bottom + pad_y),
    )
    return image.crop(box)


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, fnt, fill=INK) -> None:
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((CARD[0] - (box[2] - box[0])) / 2, y), text, font=fnt, fill=fill)


def corner(draw: ImageDraw.ImageDraw, label: str, accent, flip: bool = False) -> None:
    layer = Image.new("RGBA", (145, 176), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((12, 8), "J", font=font(42, True), fill=INK)
    d.text((12, 58), "✦", font=font(32), fill=accent)
    d.text((12, 106), label, font=font(13, True), fill=INK)
    if flip:
        layer = layer.rotate(180)
        draw._image.alpha_composite(layer, (CARD[0] - 145 - 54, CARD[1] - 176 - 50))
    else:
        draw._image.alpha_composite(layer, (54, 50))


def save_print_and_trim(card: Image.Image, out_name: str) -> Path:
    PRINT.mkdir(parents=True, exist_ok=True)
    FINAL.mkdir(parents=True, exist_ok=True)
    print_output = PRINT / out_name
    final_output = FINAL / out_name
    rgb = card.convert("RGB")
    rgb.save(print_output, quality=96, dpi=(300, 300))
    rgb.crop((BLEED, BLEED, CARD[0] - BLEED, CARD[1] - BLEED)).save(
        final_output, quality=96, dpi=(300, 300)
    )
    return final_output


def render(raw_name: str, out_name: str, joker_label: str, title: str, subtitle: str, accent) -> Path:
    card = Image.new("RGBA", CARD, BG + (255,))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        (BLEED + 10, BLEED + 10, CARD[0] - BLEED - 10, CARD[1] - BLEED - 10),
        radius=28,
        outline=(91, 88, 82),
        width=2,
    )

    corner(draw, joker_label, accent)
    corner(draw, joker_label, accent, flip=True)

    centered(draw, 96, "GGC SPIRITUALITY SERIES", font(16), fill=(82, 79, 74))
    centered(draw, 132, "FROM JOHN TO JESUS", font(15), fill=(82, 79, 74))

    art = crop_art(RAW / raw_name)
    art = ImageOps.contain(art, (520, 570), Image.Resampling.LANCZOS)
    art_layer = Image.new("RGBA", art.size, (255, 255, 255, 0))
    art_rgba = art.convert("RGBA")
    # Remove the generated pure-white field so the card's warm paper stays consistent.
    pixels = art_rgba.load()
    for y in range(art_rgba.height):
        for x in range(art_rgba.width):
            r, g, b, _ = pixels[x, y]
            alpha = max(0, min(255, (255 - min(r, g, b)) * 12))
            pixels[x, y] = (r, g, b, alpha)
    art_layer.alpha_composite(art_rgba)
    card.alpha_composite(art_layer, ((CARD[0] - art.width) // 2, 258 + (570 - art.height) // 2))

    centered(draw, 852, title, font(34, True), fill=accent)
    centered(draw, 906, subtitle, font(16), fill=INK)
    centered(draw, 966, "CONTEMPORARY SYMBOLIC DESIGN · NO VERSE CLAIM", font(13), fill=(94, 90, 84))
    centered(draw, 1001, "Companion deck to the 440-card text-history archive", font(12), fill=(112, 108, 101))

    return save_print_and_trim(card, out_name)


def contact_sheet(paths: list[Path]) -> None:
    cards = [Image.open(path).convert("RGB") for path in paths]
    thumb_w = 408
    thumb_h = round(TRIM[1] * thumb_w / TRIM[0])
    sheet = Image.new("RGB", (thumb_w * 2 + 72, thumb_h + 72), (235, 233, 228))
    for index, card in enumerate(cards):
        card.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(card, (24 + index * (thumb_w + 24), 24))
    PROOF.mkdir(parents=True, exist_ok=True)
    sheet.save(PROOF / "jokers-contact-sheet.jpg", quality=94)


if __name__ == "__main__":
    outputs = [
        render(
            "joker-big-love-light.png",
            "joker-big-love-light.png",
            "BIG",
            "LOVE & LIGHT",
            "A glowing heart · the deck's symbolic synthesis",
            GOLD,
        ),
        render(
            "joker-small-jesus-heart.png",
            "joker-small-jesus-heart.png",
            "SMALL",
            "JESUS · HEART",
            "A contemporary gesture of love and welcome",
            CORAL,
        ),
    ]
    contact_sheet(outputs)
