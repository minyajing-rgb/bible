#!/usr/bin/env python3
"""Create a two-sided A4 tri-fold instruction leaflet with 3 mm bleed."""

from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "print"
PDF_PATH = OUTPUT / "from-john-to-jesus-instruction-leaflet.pdf"

PAGE_W = 303 * mm
PAGE_H = 216 * mm
BLEED = 3 * mm
TRIM_W = 297 * mm
TRIM_H = 210 * mm
PANEL_W = TRIM_W / 3

BG = HexColor("#FAF9F6")
INK = HexColor("#242321")
MUTED = HexColor("#716D65")
GOLD = HexColor("#BE8E2F")
PALE_GOLD = HexColor("#F7EED4")
SKY = HexColor("#6AA9C4")
SAGE = HexColor("#77976F")
CORAL = HexColor("#C56A5A")

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("FJTJ", SANS))
pdfmetrics.registerFont(TTFont("FJTJ-Bold", SANS_BOLD))


def paragraph(canvas, text, x, y, width, height, size=8, leading=None, color=INK,
              align=TA_LEFT, bold=False):
    style = ParagraphStyle(
        name="leaflet",
        fontName="FJTJ-Bold" if bold else "FJTJ",
        fontSize=size,
        leading=leading or size * 1.35,
        textColor=color,
        alignment=align,
        spaceAfter=0,
    )
    story = Paragraph(text, style)
    story.wrapOn(canvas, width, height)
    story.drawOn(canvas, x, y + height - story.height)
    return story.height


def panel(canvas, index):
    x = BLEED + index * PANEL_W
    canvas.setStrokeColor(HexColor("#E4DED1"))
    canvas.setLineWidth(0.25)
    canvas.rect(x, BLEED, PANEL_W, TRIM_H, stroke=1, fill=0)
    return x


def sun(canvas, cx, cy, radius):
    canvas.setFillColor(PALE_GOLD)
    canvas.setStrokeColor(INK)
    canvas.setLineWidth(0.8)
    canvas.circle(cx, cy, radius, stroke=1, fill=1)
    canvas.setStrokeColor(GOLD)
    canvas.circle(cx, cy, radius * 0.72, stroke=1, fill=0)
    for angle in range(0, 360, 30):
        import math
        a = math.radians(angle)
        canvas.line(
            cx + math.cos(a) * radius * 1.22,
            cy + math.sin(a) * radius * 1.22,
            cx + math.cos(a) * radius * 1.55,
            cy + math.sin(a) * radius * 1.55,
        )
    canvas.setFillColor(GOLD)
    canvas.circle(cx, cy, 1.2 * mm, stroke=0, fill=1)


def page_background(canvas):
    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setStrokeColor(HexColor("#B8B1A4"))
    canvas.setDash(2, 2)
    canvas.rect(BLEED, BLEED, TRIM_W, TRIM_H, stroke=1, fill=0)
    for i in (1, 2):
        x = BLEED + i * PANEL_W
        canvas.line(x, BLEED, x, BLEED + TRIM_H)
    canvas.setDash()


def cover_panel(canvas, x):
    cx = x + PANEL_W / 2
    sun(canvas, cx, BLEED + 142 * mm, 13 * mm)
    paragraph(canvas, "GGC SPIRITUALITY SERIES", x + 10*mm, BLEED + 112*mm,
              PANEL_W - 20*mm, 10*mm, 8, align=TA_CENTER, color=MUTED)
    paragraph(canvas, "FROM JOHN TO JESUS", x + 8*mm, BLEED + 89*mm,
              PANEL_W - 16*mm, 18*mm, 17, leading=20, align=TA_CENTER, bold=True)
    paragraph(canvas, "THE WITNESS · THE WATER · THE LIGHT", x + 8*mm, BLEED + 75*mm,
              PANEL_W - 16*mm, 12*mm, 7.5, align=TA_CENTER, bold=True, color=GOLD)
    paragraph(canvas, "54-CARD GOSPEL DECK<br/>INSTRUCTION & SOURCE GUIDE", x + 10*mm,
              BLEED + 47*mm, PANEL_W - 20*mm, 20*mm, 10, leading=14,
              align=TA_CENTER, bold=True)
    paragraph(canvas, "John means John the Baptist.", x + 10*mm, BLEED + 27*mm,
              PANEL_W - 20*mm, 10*mm, 8, align=TA_CENTER)
    paragraph(canvas, "bible.saga1001.com", x + 10*mm, BLEED + 13*mm,
              PANEL_W - 20*mm, 8*mm, 8.5, align=TA_CENTER, bold=True, color=GOLD)


def back_panel(canvas, x):
    paragraph(canvas, "SOURCE INTEGRITY", x + 9*mm, BLEED + 172*mm,
              PANEL_W - 18*mm, 12*mm, 13, bold=True)
    paragraph(canvas,
              "This deck uses the <b>earliest recoverable Greek text</b>, not a claim that a lost physical autograph survives unchanged.",
              x + 9*mm, BLEED + 139*mm, PANEL_W - 18*mm, 30*mm, 8.2, leading=11)
    paragraph(canvas,
              "It distinguishes:<br/>1. Historical tradition<br/>2. Gospel redaction<br/>3. Scribal variant<br/>4. Later interpretation",
              x + 9*mm, BLEED + 92*mm, PANEL_W - 18*mm, 42*mm, 8.2, leading=12)
    paragraph(canvas,
              "The four Gospels are four literary witnesses, not four fully independent votes. Matthew and Luke reuse Mark and other traditions; John reframes the baptism as witness.",
              x + 9*mm, BLEED + 49*mm, PANEL_W - 18*mm, 39*mm, 8.2, leading=11)
    paragraph(canvas,
              "Critical-text basis: SBLGNT v1.2<br/>Full Greek, parallels and transmission notes:<br/><b>bible.saga1001.com</b>",
              x + 9*mm, BLEED + 17*mm, PANEL_W - 18*mm, 28*mm, 7.4, leading=10, color=MUTED)


def flap_panel(canvas, x):
    paragraph(canvas, "HOW TO USE THE DECK", x + 9*mm, BLEED + 172*mm,
              PANEL_W - 18*mm, 12*mm, 13, bold=True)
    items = [
        ("STORY ORDER", "Lay each suit A through K to follow that Gospel's John-to-Jesus sequence."),
        ("FOUR-WAY READING", "Compare the same event across suits and notice what each author retains, adds, relocates or reframes."),
        ("SOURCE STUDY", "Use the verse and archive ID on each card to open its Greek text and version history."),
        ("PLAY", "The deck keeps standard ranks and suits, so it may also be used as an ordinary 54-card deck."),
    ]
    y = BLEED + 150*mm
    for title, body in items:
        paragraph(canvas, title, x + 9*mm, y, PANEL_W - 18*mm, 8*mm, 8, bold=True, color=GOLD)
        paragraph(canvas, body, x + 9*mm, y - 20*mm, PANEL_W - 18*mm, 18*mm, 7.7, leading=10)
        y -= 37*mm


def map_panel(canvas, x):
    paragraph(canvas, "FOUR GOSPELS · FOUR SUITS", x + 9*mm, BLEED + 172*mm,
              PANEL_W - 18*mm, 12*mm, 12.5, bold=True)
    rows = [
        ("♠  MARK", SKY, "Earliest extant narrative spine · c. 65–75 CE"),
        ("♦  MATTHEW", GOLD, "Explanation, fulfillment and explicit additions · c. 80–95 CE"),
        ("♣  LUKE", SAGE, "Social ethics, prayer and returned testimony · c. 80–95 CE"),
        ("♥  JOHN", CORAL, "Witness, light and theological reframing · c. 90–100 CE"),
    ]
    y = BLEED + 148*mm
    for label, color, body in rows:
        canvas.setFillColor(color)
        canvas.circle(x + 13*mm, y + 6*mm, 3.2*mm, stroke=0, fill=1)
        paragraph(canvas, label, x + 21*mm, y, PANEL_W - 30*mm, 10*mm, 9, bold=True, color=color)
        paragraph(canvas, body, x + 21*mm, y - 17*mm, PANEL_W - 30*mm, 16*mm, 7.4, leading=9.5)
        y -= 34*mm
    paragraph(canvas, "Editorial navigation, not equal historical weight.", x + 9*mm,
              BLEED + 7*mm, PANEL_W - 18*mm, 10*mm, 7.5, color=MUTED, align=TA_CENTER)


def anatomy_panel(canvas, x):
    paragraph(canvas, "READING ONE CARD", x + 9*mm, BLEED + 172*mm,
              PANEL_W - 18*mm, 12*mm, 13, bold=True)
    y0 = BLEED + 56*mm
    canvas.setStrokeColor(INK)
    canvas.setLineWidth(0.7)
    canvas.roundRect(x + 18*mm, y0, PANEL_W - 36*mm, 102*mm, 3*mm, stroke=1, fill=0)
    paragraph(canvas, "8  ♦", x + 23*mm, y0 + 84*mm, 24*mm, 12*mm, 13, bold=True)
    paragraph(canvas, "MATTHEW", x + 38*mm, y0 + 87*mm, 35*mm, 8*mm, 7, bold=True, color=GOLD, align=TA_CENTER)
    canvas.setStrokeColor(HexColor("#B8B1A4"))
    canvas.line(x + 31*mm, y0 + 57*mm, x + PANEL_W - 31*mm, y0 + 57*mm)
    paragraph(canvas, "STORY IMAGE", x + 25*mm, y0 + 42*mm, PANEL_W - 50*mm, 10*mm, 7, color=MUTED, align=TA_CENTER)
    paragraph(canvas, "I need to be baptized by you...", x + 23*mm, y0 + 27*mm,
              PANEL_W - 46*mm, 12*mm, 7.2, align=TA_CENTER)
    paragraph(canvas, "Matthew 3:14 · c. 80–95 CE", x + 23*mm, y0 + 17*mm,
              PANEL_W - 46*mm, 7*mm, 6.4, align=TA_CENTER, color=GOLD)
    paragraph(canvas, "MATTHEAN REDACTION", x + 23*mm, y0 + 7*mm,
              PANEL_W - 46*mm, 7*mm, 6.4, align=TA_CENTER, bold=True)
    paragraph(canvas,
              "The card shows a concise quotation. The archive holds the full Greek unit, exact speaker, parallels, source status and version-history note.",
              x + 9*mm, BLEED + 18*mm, PANEL_W - 18*mm, 30*mm, 7.7, leading=10.5)


def labels_panel(canvas, x):
    paragraph(canvas, "SOURCE LABELS", x + 9*mm, BLEED + 172*mm,
              PANEL_W - 18*mm, 12*mm, 13, bold=True)
    labels = [
        ("EARLIEST EXTANT NARRATIVE", "Mark's surviving narrative spine."),
        ("MULTIPLE SYNOPTIC ATTESTATION", "Shared material with literary dependence noted."),
        ("MATTHEAN / LUKAN REDACTION", "A later author's documented literary framing."),
        ("JOHANNINE REFRAMING", "The baptism becomes remembered witness."),
        ("TEXTUAL VARIANT", "Ancient manuscripts preserve concrete alternative readings."),
        ("SOURCE CAUTION", "A single-source tradition is not independently confirmed. No secret editor is invented where evidence identifies none."),
    ]
    y = BLEED + 150*mm
    for title, body in labels:
        paragraph(canvas, title, x + 9*mm, y, PANEL_W - 18*mm, 7*mm, 7.3, bold=True, color=GOLD)
        paragraph(canvas, body, x + 9*mm, y - 13*mm, PANEL_W - 18*mm, 12*mm, 7.2, leading=9)
        y -= 25*mm


def render():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(PDF_PATH), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    canvas.setTitle("From John to Jesus · Instruction and Source Guide")

    page_background(canvas)
    back_panel(canvas, panel(canvas, 0))
    cover_panel(canvas, panel(canvas, 1))
    flap_panel(canvas, panel(canvas, 2))
    canvas.showPage()

    page_background(canvas)
    map_panel(canvas, panel(canvas, 0))
    anatomy_panel(canvas, panel(canvas, 1))
    labels_panel(canvas, panel(canvas, 2))
    canvas.showPage()
    canvas.save()
    print(PDF_PATH)


if __name__ == "__main__":
    render()
