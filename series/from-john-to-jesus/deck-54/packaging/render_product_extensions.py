#!/usr/bin/env python3
"""Render linen-bag artwork/mockup and four product-promotion images."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
BAG_PRINT = HERE / "bag" / "print"
BAG_PROOF = HERE / "bag" / "proof"
MARKETING = ROOT / "marketing"
GUIDE_PROOF = ROOT / "guide" / "proof"

BG = (250, 249, 246)
INK = (35, 34, 32)
MUTED = (111, 106, 97)
GOLD = (190, 142, 47)
PALE_GOLD = (248, 239, 207)
LINEN = (214, 199, 169)
LINEN_DARK = (159, 137, 101)
SKY = (104, 169, 197)
SAGE = (119, 151, 111)
CORAL = (197, 106, 90)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False):
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def center(draw, y, text, fnt, fill=INK, bounds=(0, 1350)):
    box = draw.textbbox((0, 0), text, font=fnt)
    x = bounds[0] + ((bounds[1] - bounds[0]) - (box[2] - box[0])) / 2
    draw.text((x, y), text, font=fnt, fill=fill)


def fit_contain(path: Path, box, background=None):
    image = Image.open(path).convert("RGBA")
    w, h = box[2] - box[0], box[3] - box[1]
    image.thumbnail((w, h), Image.Resampling.LANCZOS)
    if background is None:
        return image, (box[0] + (w - image.width)//2, box[1] + (h - image.height)//2)
    layer = Image.new("RGBA", (w, h), background)
    layer.alpha_composite(image, ((w-image.width)//2, (h-image.height)//2))
    return layer, (box[0], box[1])


def heart_points(cx, cy, scale, invert=False):
    points = []
    for i in range(181):
        t = 2 * math.pi * i / 180
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        px, py = cx + x * scale, cy - y * scale
        if invert:
            px, py = 2*cx-px, 2*cy-py
        points.append((px, py))
    return points


def sun(draw, cx, cy, radius, line=INK, accent=GOLD, fill=PALE_GOLD, width=4):
    draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill=fill, outline=line, width=width)
    draw.ellipse((cx-radius*.76, cy-radius*.76, cx+radius*.76, cy+radius*.76), outline=accent, width=max(2,width))
    for angle in range(0, 360, 15):
        a = math.radians(angle)
        inner = radius*1.18
        outer = radius*(1.52 if angle%30==0 else 1.36)
        draw.line((cx+math.cos(a)*inner, cy+math.sin(a)*inner,
                   cx+math.cos(a)*outer, cy+math.sin(a)*outer),
                  fill=accent if angle%30==0 else line, width=max(2,width//2))
    scale = radius / 42
    draw.line(heart_points(cx, cy-radius*.25, scale), fill=line, width=max(2,width), joint="curve")
    draw.line(heart_points(cx, cy+radius*.25, scale, True), fill=line, width=max(2,width), joint="curve")
    draw.ellipse((cx-5,cy-5,cx+5,cy+5),fill=accent)


def render_bag_artwork():
    image = Image.new("RGBA", (1800, 2400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    sun(draw, 900, 720, 260, fill=(0,0,0,0), width=10)
    center(draw, 1110, "GGC SPIRITUALITY SERIES", font(45), INK, (0,1800))
    center(draw, 1240, "FROM JOHN TO JESUS", font(78, True), INK, (0,1800))
    center(draw, 1380, "THE WITNESS · THE WATER · THE LIGHT", font(36, True), GOLD, (0,1800))
    center(draw, 1610, "bible.saga1001.com", font(42, True), INK, (0,1800))
    image.save(BAG_PRINT / "linen-bag-two-color-artwork.png", dpi=(300,300))


def render_bag_mockup():
    image = Image.new("RGB", (1200, 1500), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((230,190,970,1330),radius=45,fill=LINEN,outline=LINEN_DARK,width=4)
    draw.polygon([(230,260),(175,330),(230,385)],fill=LINEN,outline=LINEN_DARK)
    draw.polygon([(970,260),(1025,330),(970,385)],fill=LINEN,outline=LINEN_DARK)
    draw.line((260,270,940,270),fill=LINEN_DARK,width=8)
    draw.line((260,270,165,185),fill=LINEN_DARK,width=6)
    draw.line((940,270,1035,185),fill=LINEN_DARK,width=6)
    draw.ellipse((140,155,190,205),outline=LINEN_DARK,width=5)
    draw.ellipse((1010,155,1060,205),outline=LINEN_DARK,width=5)
    sun(draw,600,600,125,fill=LINEN,width=5)
    center(draw,795,"FROM JOHN TO JESUS",font(38,True),INK,(230,970))
    center(draw,865,"THE WITNESS · THE WATER · THE LIGHT",font(18,True),GOLD,(230,970))
    center(draw,1040,"54-CARD GOSPEL DECK",font(24,True),INK,(230,970))
    center(draw,1100,"bible.saga1001.com",font(22),MUTED,(230,970))
    center(draw,1395,"UNBLEACHED LINEN · REUSABLE DRAWSTRING BAG",font(20,True),MUTED,(0,1200))
    image.save(BAG_PROOF / "linen-bag-mockup.png", dpi=(300,300))


def base_promo(kicker, title, subtitle):
    image = Image.new("RGB", (1350,1688), BG)
    draw = ImageDraw.Draw(image)
    center(draw,70,kicker,font(22,True),MUTED)
    center(draw,125,title,font(52,True),INK)
    center(draw,205,subtitle,font(23,True),GOLD)
    return image, draw


def promo_hero():
    image, draw = base_promo("GGC SPIRITUALITY SERIES","FROM JOHN TO JESUS","A 54-CARD SOURCE-LAYERED GOSPEL DECK")
    cards = [
        ROOT/"final"/"joker-big-love-light.png",
        ROOT/"final"/"ace-spades-mark.png",
        ROOT/"final"/"ace-diamonds-matthew.png",
        ROOT/"final"/"ace-clubs-luke.png",
        ROOT/"final"/"ace-hearts-john.png",
    ]
    for i,path in enumerate(cards):
        card=Image.open(path).convert("RGBA").resize((245,342),Image.Resampling.LANCZOS)
        image.paste(card,(45+i*255,360),card)
    box=Image.open(HERE/"final"/"tuck-box-front.png").convert("RGBA")
    box.thumbnail((330,470),Image.Resampling.LANCZOS)
    image.paste(box,(165,835),box)
    bag=Image.open(BAG_PROOF/"linen-bag-mockup.png").convert("RGBA")
    bag.thumbnail((330,430),Image.Resampling.LANCZOS)
    image.paste(bag,(510,820),bag)
    leaflet=Image.open(GUIDE_PROOF/"instruction-leaflet-outside.png").convert("RGBA")
    leaflet.thumbnail((420,300),Image.Resampling.LANCZOS)
    image.paste(leaflet,(850,900),leaflet)
    center(draw,1345,"54 CARDS · TUCK BOX · REUSABLE LINEN BAG · SOURCE GUIDE",font(24,True),INK)
    center(draw,1410,"EARLIEST RECOVERABLE GREEK · REDACTION · VARIANTS · WITNESS",font(19),MUTED)
    center(draw,1525,"bible.saga1001.com",font(30,True),GOLD)
    image.save(MARKETING/"promo-01-complete-product-system.png",dpi=(300,300))


def promo_four_gospels():
    image,draw=base_promo("FROM JOHN TO JESUS","FOUR GOSPELS · FOUR LENSES","ONE DECK · SOURCE DIFFERENCES KEPT VISIBLE")
    paths=[
        (ROOT/"final"/"ace-spades-mark.png",SKY,"MARK · c. 65–75 CE"),
        (ROOT/"final"/"ace-diamonds-matthew.png",GOLD,"MATTHEW · c. 80–95 CE"),
        (ROOT/"final"/"ace-clubs-luke.png",SAGE,"LUKE · c. 80–95 CE"),
        (ROOT/"final"/"ace-hearts-john.png",CORAL,"JOHN · c. 90–100 CE"),
    ]
    for i,(path,color,label) in enumerate(paths):
        x=135+(i%2)*570; y=340+(i//2)*570
        card=Image.open(path).convert("RGBA"); card.thumbnail((330,460),Image.Resampling.LANCZOS)
        image.paste(card,(x,y),card)
        draw.rounded_rectangle((x+350,y+150,x+520,y+220),radius=24,fill=color)
        bb=draw.textbbox((0,0),label,font=font(15,True)); tw=bb[2]-bb[0]
        draw.text((x+435-tw/2,y+175),label,font=font(15,True),fill=(255,255,255))
    center(draw,1510,"EDITORIAL NAVIGATION · NOT FOUR FULLY INDEPENDENT VOTES",font(21,True),MUTED)
    image.save(MARKETING/"promo-02-four-gospels-four-suits.png",dpi=(300,300))


def promo_text_history():
    image,draw=base_promo("FROM JOHN TO JESUS","WHAT CHANGED — AND WHAT DID NOT","HISTORICAL TRADITION ≠ GOSPEL REDACTION ≠ SCRIBAL VARIANT")
    examples=[
        (ROOT/"final"/"spades-8-mark.png","MARK 1:9","John directly baptizes Jesus.",SKY),
        (ROOT/"final"/"diamonds-8-matthew.png","MATTHEW 3:14","The author adds John's objection.",GOLD),
        (ROOT/"final"/"diamonds-9-matthew.png","MATTHEW 3:15","The author adds Jesus' answer.",GOLD),
    ]
    for i,(path,head,body,color) in enumerate(examples):
        x=80+i*425
        card=Image.open(path).convert("RGBA"); card.thumbnail((330,460),Image.Resampling.LANCZOS)
        image.paste(card,(x,350),card)
        draw.text((x,850),head,font=font(24,True),fill=color)
        draw.multiline_text((x,900),body,font=font(19),fill=INK,spacing=8)
    y=1115
    rows=[
        ("EARLIEST RECOVERABLE GREEK","Critical text reconstructed from surviving manuscripts."),
        ("AUTHORIAL REDACTION","How a Gospel author selects, arranges and explains material."),
        ("SCRIBAL VARIANT","A concrete alternative reading preserved by manuscript witnesses."),
    ]
    for head,body in rows:
        draw.rounded_rectangle((110,y,1240,y+115),radius=20,fill=(246,243,235),outline=(221,214,199),width=2)
        draw.text((145,y+23),head,font=font(22,True),fill=GOLD)
        draw.text((145,y+65),body,font=font(18),fill=MUTED)
        y+=135
    image.save(MARKETING/"promo-03-text-history-system.png",dpi=(300,300))


def promo_print_ready():
    image,draw=base_promo("FROM JOHN TO JESUS","BUILT FOR PRINT · CHECKED FOR SOURCES","63 × 88 mm TRIM · 3 mm BLEED · 300 DPI")
    back=Image.open(ROOT/"final"/"card-back.png").convert("RGBA"); back.thumbnail((390,545),Image.Resampling.LANCZOS)
    card=Image.open(ROOT/"final"/"diamonds-9-matthew.png").convert("RGBA"); card.thumbnail((390,545),Image.Resampling.LANCZOS)
    image.paste(back,(190,350),back); image.paste(card,(770,350),card)
    lines=[
        ("54-CARD MAP","52 suited cards + 2 symbolic Jokers"),
        ("SOURCE GATE","Exact verse, speaker, quote type and layer"),
        ("TWO CONTENT PASSES","Greek/text first; context/redaction second"),
        ("POST-LAYOUT CHECK","Trim pair, bleed, safe zone and rendered quote"),
    ]
    y=1035
    for head,body in lines:
        draw.ellipse((135,y+4,155,y+24),fill=GOLD)
        draw.text((185,y),head,font=font(23,True),fill=INK)
        draw.text((520,y+2),body,font=font(20),fill=MUTED)
        y+=100
    center(draw,1510,"PRODUCTION PROOF · FINAL TUCK-BOX DIELINE MUST COME FROM THE PRINTER",font(20,True),GOLD)
    image.save(MARKETING/"promo-04-print-and-audit.png",dpi=(300,300))


def render_all():
    for folder in (BAG_PRINT,BAG_PROOF,MARKETING): folder.mkdir(parents=True,exist_ok=True)
    render_bag_artwork()
    render_bag_mockup()
    promo_hero()
    promo_four_gospels()
    promo_text_history()
    promo_print_ready()
    print("Rendered linen-bag package and four promotional images.")


if __name__ == "__main__":
    render_all()
