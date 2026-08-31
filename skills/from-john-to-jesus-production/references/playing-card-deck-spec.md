# Gospel Playing-Card Mode

Read this file only when producing the 54-card companion deck.

Use `series/from-john-to-jesus/deck-54/ledger.json` as the fixed card map and `docs/54-card-gospel-deck-blueprint.md` as the print/layout contract.

## Invariants

- 54 cards exactly: 52 suited cards plus two Jokers.
- Spades = Mark; Diamonds = Matthew; Clubs = Luke; Hearts = John.
- Suits are navigation categories, not four independent historical votes.
- One central sourced scene per suited card; no invented dialogue.
- Big Joker is a contemporary editorial symbol, not an ancient quotation.
- Small Joker's finger-heart is labeled contemporary; never cite it as a Gospel action.
- Actual variants receive a `VARIANT` badge and link to the full evidence record.
- Render all rank, suit, English, Greek, verse, and badges deterministically.
- Print at 63 × 88 mm with 3 mm bleed; deliver fronts, back, contact sheet, and proof PDF.
- Keep rank and suit inside the trim-safe zone. On the 69 × 94 mm print canvas,
  the first 3 mm on every side are bleed and may be cut away; no essential mark
  may sit there.
- The common back is a two-way rotationally symmetric sun. If hearts are used at
  its center, use two clean pointed hearts whose tips overlap slightly; do not
  replace the sun with a large heart emblem.

## Two-pass content gate

Every suited card must pass two recorded checks before image generation:

1. `PASS_1_TEXT`: reference, exact Greek unit, speaker/narrator boundary, quote
   type, and literal English checked against the selected critical text.
2. `PASS_2_CONTEXT`: scene, chronology, Gospel layer, literary dependence,
   parallels, and any variant/redaction caution checked independently a second
   time.

Store the result in `series/from-john-to-jesus/deck-54/audit/verified-cards.json`.
Do not render a suited card unless both statuses are `PASS`. Re-run the audit
after typography and visual compositing; a source-correct ledger does not make a
misleading picture acceptable.

## Production order

1. Lock the common back and character proportions.
2. Produce Jokers and four Aces as the style proof.
3. Complete one Gospel as a coherent A–K sequence before moving to the next:
   Mark/Spades → Matthew/Diamonds → Luke/Clubs → John/Hearts.
4. For each Gospel, second-check all thirteen content records before producing
   its remaining art.
5. Audit source identity, trim-safe spacing, and 3 mm bleed after every batch.
6. Do not publish a partial set as a final deck; label interim outputs `PROOF`.

## Packaging gate

The 54-card deck includes a tuck box. Use the same warm-white, charcoal, and
pale-gold sun system as the common back. The front carries the series title;
the back carries the four-Gospel suit map and the source-integrity statement;
the sides carry the series and subtitle. Keep all essential text inside the
vendor's safe zone and extend background artwork through 3 mm bleed.

The repository may contain a generic review dieline, but mass-production files
must use the selected printer's certified AI/PDF dieline. Confirm card stock,
finished internal depth, glue flap, tuck flap, bottom lock, CMYK profile, QR/URL,
and a fully loaded physical proof before print approval.
