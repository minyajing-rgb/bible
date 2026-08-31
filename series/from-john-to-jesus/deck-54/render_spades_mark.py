#!/usr/bin/env python3
"""Render the verified Mark/Spades A–K sequence with bleed and trim outputs."""

from pathlib import Path

from render_aces_and_back import CARDS, PROOF, SKY, contact_sheet, render_front


ROOT = Path(__file__).resolve().parent

MARK_CARDS = [
    CARDS[0],
    {
        "id": "SP-2", "rank": "2", "suit": "♠", "gospel": "MARK",
        "raw": "spades-2-mark.png", "output": "spades-2-mark.png",
        "title": "JOHN APPEARED",
        "quote": "John came, baptizing in the wilderness.",
        "source": "Mark 1:4", "layer": "EARLIEST EXTANT NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-3", "rank": "3", "suit": "♠", "gospel": "MARK",
        "raw": "spades-3-mark.png", "output": "spades-3-mark.png",
        "title": "CROWDS AT THE JORDAN",
        "quote": "They were baptized by him in the Jordan.",
        "source": "Mark 1:5", "layer": "EARLIEST EXTANT NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-4", "rank": "4", "suit": "♠", "gospel": "MARK",
        "raw": "spades-4-mark.png", "output": "spades-4-mark.png",
        "title": "CAMEL HAIR AND WILD HONEY",
        "quote": "He was clothed with camel hair and a leather belt.",
        "source": "Mark 1:6", "layer": "EARLIEST EXTANT NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-5", "rank": "5", "suit": "♠", "gospel": "MARK",
        "raw": "spades-5-mark.png", "output": "spades-5-mark.png",
        "title": "THE STRONGER ONE COMES",
        "quote": "The stronger one than I comes after me.",
        "source": "Mark 1:7", "layer": "MULTIPLE-GOSPEL MOTIF",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-6", "rank": "6", "suit": "♠", "gospel": "MARK",
        "raw": "spades-6-mark.png", "output": "spades-6-mark.png",
        "title": "WATER AND SPIRIT",
        "quote": "I baptized you with water; he will baptize you with holy spirit.",
        "source": "Mark 1:8", "layer": "EARLY SHARED TRADITION",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-7", "rank": "7", "suit": "♠", "gospel": "MARK",
        "raw": "spades-7-mark.png", "output": "spades-7-mark.png",
        "title": "JESUS COMES FROM NAZARETH",
        "quote": "Jesus came from Nazareth of Galilee.",
        "source": "Mark 1:9a", "layer": "EARLIEST EXTANT BAPTISM NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-8", "rank": "8", "suit": "♠", "gospel": "MARK",
        "raw": "spades-8-mark.png", "output": "spades-8-mark.png",
        "title": "BAPTIZED BY JOHN",
        "quote": "He was baptized in the Jordan by John.",
        "source": "Mark 1:9b", "layer": "EARLIEST EXTANT BAPTISM NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-9", "rank": "9", "suit": "♠", "gospel": "MARK",
        "raw": "spades-9-mark.png", "output": "spades-9-mark.png",
        "title": "HEAVENS TORN OPEN",
        "quote": "He saw the heavens being torn apart.",
        "source": "Mark 1:10a", "layer": "EARLIEST EXTANT BAPTISM NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-10", "rank": "10", "suit": "♠", "gospel": "MARK",
        "raw": "spades-10-mark.png", "output": "spades-10-mark.png",
        "title": "YOU ARE MY BELOVED SON",
        "quote": "You are my beloved Son; in you I delighted.",
        "source": "Mark 1:11", "layer": "EARLIEST EXTANT BAPTISM NARRATIVE",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-J", "rank": "J", "suit": "♠", "gospel": "MARK",
        "raw": "spades-j-mark.png", "output": "spades-j-mark.png",
        "title": "AFTER JOHN WAS HANDED OVER",
        "quote": "After John was handed over, Jesus came into Galilee.",
        "source": "Mark 1:14", "layer": "MARKAN HANDOVER",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-Q", "rank": "Q", "suit": "♠", "gospel": "MARK",
        "raw": "spades-q-mark.png", "output": "spades-q-mark.png",
        "title": "JOHN CHALLENGES HEROD",
        "quote": "It is not lawful for you to have your brother's wife.",
        "source": "Mark 6:18", "layer": "EARLIEST EXTANT CONFLICT ACCOUNT",
        "date": "c. 65–75 CE", "accent": SKY,
    },
    {
        "id": "SP-K", "rank": "K", "suit": "♠", "gospel": "MARK",
        "raw": "spades-k-mark.png", "output": "spades-k-mark.png",
        "title": "THE FORERUNNER IS BURIED",
        "quote": "They took his body and placed it in a tomb.",
        "source": "Mark 6:29", "layer": "EARLIEST EXTANT DEATH ACCOUNT",
        "date": "c. 65–75 CE", "accent": SKY,
    },
]


if __name__ == "__main__":
    outputs = [render_front(data) for data in MARK_CARDS]
    contact_sheet(outputs, "spades-mark-a-k-contact-sheet.jpg", columns=4)
    print(f"Rendered {len(outputs)} verified Mark/Spades cards to print/ and final/.")
