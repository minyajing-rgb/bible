---
name: from-john-to-jesus-production
description: Plan, research, produce, audit, and publish the 44-chapter GGC “From John to Jesus” text-history archive. Every card shows the earliest recoverable Greek, a literal English rendering, a sourced scene, and an evidence-labeled change timeline. John is always John the Baptist; never the apostle or beloved disciple.
---

# From John to Jesus Production

Produce one complete chapter of 10 separate 4:5 final PNG evidence cards at a time. A chapter is not complete until its images, ledger rows, chapter README, progress index, and portal index agree.

For the separate 54-card companion playing deck, read [Gospel playing-card mode](references/playing-card-deck-spec.md). The deck uses the same identity and source gates but has its own print dimensions and fixed four-suit map.

## Primary purpose

This is a public-facing textual-history archive, not a generic devotional illustration series. Its central claim is deliberately narrow:

> A familiar church translation is a later edition, not the lost physical autograph. The project shows the earliest recoverable Greek text and the evidence trail by which Gospel redaction, manuscript variants, and later translation choices can be distinguished.

Never promise an “unchanged original.” No New Testament autograph survives. Use `EARLIEST RECOVERABLE GREEK` and identify the critical edition or manuscript witness used.

## Editorial hierarchy

The fixed hierarchy is:

```text
Series → 7 Parts → 44 Chapters/Batches → 10 Cards per Chapter → 440 Cards
```

Before planning or changing a chapter, read [editorial architecture](references/editorial-architecture.md). Then read [text history and variant method](references/text-history-and-variant-method.md), [three-zone card system](references/three-zone-card-system.md), and [chapter template and sample](references/chapter-template-and-sample.md). Classify by reader journey, chronology, and source layer before applying the spiritual theme.

## Deliverable invariant

`raw/` contains internal no-text illustration assets only. Never show, publish, upload, or hand off a raw illustration as a finished card. The user-facing deliverable is always `final/`, after deterministic typography has been applied.

Every final card has three visibly separate zones. It must contain all of the following:

- **Top · TEXT:** chapter/verse, earliest recoverable Greek, literal English, speaker, source layer, approximate composition date, and critical-text basis.
- **Middle · SCENE:** one sourced historical action or a clearly labeled evidence diagram.
- **Bottom · CHANGE RECORD:** a dated mini-timeline whose entries identify `GOSPEL_REDACTION`, `SCRIBAL_VARIANT`, or `TRANSLATION_HISTORY`, with witnesses and uncertainty.

Use explicit labels. Do not compress evidence into an unlabeled microtype footer. A card that contains the data in the ledger but does not display all three zones readably is incomplete.

## Identity invariant

`John` means `JOHN_BAPTIST`. Never substitute `JOHN_ZEBEDEE`, `BELOVED_DISCIPLE`, or `JOHANNINE_AUTHOR`. Remove last-supper, cross, empty-tomb, and resurrection-breakfast material from this series.

## Reader-journey invariant

Begin with the four canonical Gospel accounts and mainstream common ground so church readers can first see what the sources share and where they depend on one another. Then move through John's own words, John–Jesus dialogue, Jesus' answer in deeds and the returned report, John's death and handover, Jesus after John using Mark as the earliest extant narrative spine, and only at the end the later Johannine light-and-love layer. Luke's infancy material is a labeled appendix, not the canonical opening.

## Required workflow

1. Read [source and identity gates](references/source-and-identity-gates.md).
2. Read [editorial architecture](references/editorial-architecture.md), locate the next chapter in its Part, and inspect `docs/44-batch-roadmap.md` plus the ledger for duplicates.
3. Read [text history and variant method](references/text-history-and-variant-method.md). Verify the Greek and all historical claims against primary manuscript/critical-edition evidence and authoritative scholarship. Record uncertainty instead of resolving disputes rhetorically.
4. Read [chapter template and sample](references/chapter-template-and-sample.md). Write the chapter's central question, one-sentence claim, source spine, later layers, exclusions, opening state, ending state, ten-card function map, and change-track entries before drafting any image prompt.
5. Reject a source-accurate chapter if it sits on the wrong narrative branch or imports a later source layer without labeling it.
6. Read [visual and batch specification](references/visual-and-batch-spec.md), [three-zone card system](references/three-zone-card-system.md), and inspect `assets/approved-minimal-line-style.png`.
7. Build 10 ledger rows before generating images. Each row has one beat, one scene, one speaker/narrator or evidence unit, one text unit, and one or more dated change-track entries.
8. Generate 10 separate no-text illustrations, one call per asset. Pass the approved style anchor into every generation call; after card 01 is accepted, pass it as the character anchor too.
9. Reject and regenerate any image with shading, realistic anatomy, detailed architecture, oversized figures, multiple accent hues, or invented people/props.
10. Render exact typography and timeline deterministically with `scripts/render_cards.py`; never ask the image model to spell Greek, dates, witnesses, notes, or branding.
11. Verify all 10 final cards as a contact sheet and at full size, then audit with `scripts/audit_batch.py`. The audit must fail if a card lacks any of the three zones or a change entry lacks category, date, witness, and statement.
12. Update repository and portal progress only after all ten final files exist and the chapter conclusion matches its evidence-bounded claim.

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

## Change-track labels

- `GOSPEL_REDACTION` — one Gospel author adapts, omits, adds, or reframes inherited tradition. Use approximate Gospel composition dates.
- `SCRIBAL_VARIANT` — surviving manuscript witnesses preserve different readings of the same passage. Name witnesses when securely identifiable; do not invent the scribe.
- `TRANSLATION_HISTORY` — later printed editions or translations select/render a reading. Name the edition and publication year; do not present translation wording as an ancient manuscript.

If a card has no documented wording change, its timeline still records the earliest extant account and the relationship of later Gospel tellings. Never fabricate a variant to fill the bottom zone.

## Stop conditions

Do not publish if any card has the wrong John, assigns narration to a character, claims independent attestation where sources are literarily dependent, invents a dialogue, contains malformed Greek, calls a modern critical edition “the autograph,” merges authorial redaction with scribal variation, assigns an anonymous change to a named church official, omits the source caution for a single-source tradition, drifts from the approved visual reference, exposes a raw no-text illustration, or renders any evidence field too small to read.
