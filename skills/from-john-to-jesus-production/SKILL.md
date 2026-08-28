---
name: from-john-to-jesus-production
description: Produce, audit, and publish 10-card batches for GGC Spirituality Series “From John to Jesus,” with John fixed as John the Baptist, source-layer labeling, exact speaker identity, and the approved ultra-minimal black-line visual system. Use for this exact 44-batch series; do not use for apostle John or the beloved disciple.
---

# From John to Jesus Production

Produce one complete batch of 10 separate 4:5 final PNG cards at a time. A batch is not complete until its images, ledger rows, batch README, and progress index agree.

## Deliverable invariant

`raw/` contains internal no-text illustration assets only. Never show, publish, upload, or hand off a raw illustration as a finished card. The user-facing deliverable is always `final/`, after deterministic typography has been applied.

Every final card must visibly and legibly contain all of the following:

- literal English quotation
- earliest recoverable Greek excerpt
- source book and verse
- source layer
- approximate date
- parallel passage or an explicit `NONE`
- historical status
- the applicable source, redaction, reframing, variant, or caution note

Use explicit labels for the source block. Do not compress the fields into an unlabeled microtype footer. A card that contains the data in the ledger but does not display it readably is incomplete.

## Identity invariant

`John` means `JOHN_BAPTIST`. Never substitute `JOHN_ZEBEDEE`, `BELOVED_DISCIPLE`, or `JOHANNINE_AUTHOR`. Remove last-supper, cross, empty-tomb, and resurrection-breakfast material from this series.

## Narrative invariant

The default main line begins with the adult John in the wilderness and moves through the Jordan toward Jesus. Do not open the canonical series with Zechariah, Elizabeth, pregnancy, or John's birth. Luke's infancy material is allowed only when explicitly requested as a clearly labeled `LUKE-ONLY INFANCY TRADITION` appendix.

## Required workflow

1. Read [source and identity gates](references/source-and-identity-gates.md).
2. Read [visual and batch specification](references/visual-and-batch-spec.md) and visually inspect `assets/approved-minimal-line-style.png`. This asset is the mandatory style anchor, not optional inspiration.
3. Before selecting scenes, confirm that the batch advances the requested John-the-Baptist → Jesus arc. Reject a source-accurate batch if it is on the wrong narrative branch.
4. Select the next unfinished batch from `docs/44-batch-roadmap.md` and inspect the ledger for duplicates.
5. Build 10 ledger rows before generating images. Each row has one beat, one scene, one speaker/narrator, one exact quotation unit, and one source-status note.
6. Generate 10 separate no-text illustrations, one call per asset. Pass the approved style anchor into every generation call; after card 01 is accepted, pass it as the character anchor too.
7. Reject and regenerate any image with shading, realistic anatomy, watercolor/pencil texture, detailed architecture, oversized figures, multiple accent hues, or invented people/props.
8. Render exact typography deterministically with `scripts/render_cards.py`; do not ask the image model to spell Greek, source notes, or branding.
9. Verify all 10 final cards as a contact sheet and at full size. At contact-sheet size the quotation, verse, and source-layer category must remain identifiable; at full size every source field must be comfortably readable. Then audit the ledger with `scripts/audit_batch.py`.
10. Update repository progress only after all ten final files exist.

## Source labels

Use the narrowest applicable label:

- `EARLIEST EXTANT NARRATIVE`
- `MULTIPLE SYNOPTIC ATTESTATION`
- `MATTHEAN REDACTION`
- `LUKAN REDACTION`
- `JOHANNINE REFRAMING`
- `JOHANNINE-ONLY SAYING`
- `LUKE-ONLY INFANCY TRADITION`
- `TEXTUAL VARIANT`
- `JOSEPHUS EXTERNAL WITNESS`

Do not call Gospel redaction a later scribal change. Do not identify a named editor when the evidence supports only “the author of Matthew/Luke/John.”

## Stop conditions

Do not publish if any card has the wrong John, assigns narration to a character, claims independent attestation where sources are literarily dependent, invents a dialogue, contains malformed Greek, omits the source caution for a single-source tradition, drifts away from the approved minimalist line reference, exposes a raw no-text illustration as a deliverable, or renders any required source field too small to read.
