#!/usr/bin/env python3
"""Render Matthew/Diamonds batch 01: ranks 2 through Jack."""

from render_aces_and_back import GOLD, PROOF, contact_sheet, render_front


MATTHEW_BATCH_01 = [
    {
        "id": "DI-2", "rank": "2", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-2-matthew.png", "output": "diamonds-2-matthew.png",
        "title": "JUDEA GOES OUT TO JOHN",
        "quote": "They were baptized by him in the Jordan.",
        "source": "Matthew 3:5–6", "layer": "MATTHEAN REDACTION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-3", "rank": "3", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-3-matthew.png", "output": "diamonds-3-matthew.png",
        "title": "OFFSPRING OF VIPERS",
        "quote": "Offspring of vipers—who warned you to flee?",
        "source": "Matthew 3:7", "layer": "MULTIPLE SYNOPTIC ATTESTATION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-4", "rank": "4", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-4-matthew.png", "output": "diamonds-4-matthew.png",
        "title": "FRUIT WORTHY OF REPENTANCE",
        "quote": "Produce fruit worthy of repentance.",
        "source": "Matthew 3:8–10", "layer": "MULTIPLE SYNOPTIC ATTESTATION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-5", "rank": "5", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-5-matthew.png", "output": "diamonds-5-matthew.png",
        "title": "SPIRIT AND FIRE",
        "quote": "He will baptize you in holy spirit and fire.",
        "source": "Matthew 3:11", "layer": "MULTIPLE SYNOPTIC ATTESTATION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-6", "rank": "6", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-6-matthew.png", "output": "diamonds-6-matthew.png",
        "title": "THE WINNOWING FLOOR",
        "quote": "His winnowing fork is in his hand.",
        "source": "Matthew 3:12", "layer": "MULTIPLE SYNOPTIC ATTESTATION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-7", "rank": "7", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-7-matthew.png", "output": "diamonds-7-matthew.png",
        "title": "JESUS COMES TO JOHN",
        "quote": "Jesus came to John to be baptized by him.",
        "source": "Matthew 3:13", "layer": "MATTHEAN REDACTION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-8", "rank": "8", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-8-matthew.png", "output": "diamonds-8-matthew.png",
        "title": "JOHN TRIES TO PREVENT HIM",
        "quote": "I need to be baptized by you—and you come to me?",
        "source": "Matthew 3:14", "layer": "MATTHEAN REDACTION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-9", "rank": "9", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-9-matthew.png", "output": "diamonds-9-matthew.png",
        "title": "ALLOW IT NOW",
        "quote": "Allow it now—to fulfill all righteousness.",
        "source": "Matthew 3:15", "layer": "MATTHEAN REDACTION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-10", "rank": "10", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-10-matthew.png", "output": "diamonds-10-matthew.png",
        "title": "THIS IS MY BELOVED SON",
        "quote": "This is my beloved Son; in him I delighted.",
        "source": "Matthew 3:17", "layer": "MATTHEAN REDACTION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
    {
        "id": "DI-J", "rank": "J", "suit": "♦", "gospel": "MATTHEW",
        "raw": "diamonds-j-matthew.png", "output": "diamonds-j-matthew.png",
        "title": "REPORT WHAT YOU SEE",
        "quote": "Report to John what you hear and see.",
        "source": "Matthew 11:4–5", "layer": "MULTIPLE SYNOPTIC ATTESTATION",
        "date": "c. 80–95 CE", "accent": GOLD,
    },
]


if __name__ == "__main__":
    outputs = [render_front(data) for data in MATTHEW_BATCH_01]
    contact_sheet(outputs, "diamonds-matthew-2-j-contact-sheet.jpg", columns=5)
    print(f"Rendered {len(outputs)} verified Matthew/Diamonds cards to print/ and final/.")
