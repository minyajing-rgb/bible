# Text History and Variant Method

## The claim this project may make

Use **earliest recoverable Greek text**. The physical authorial manuscripts do not survive. A modern critical text such as SBLGNT, NA28, or ECM is a scholarly reconstruction made by comparing manuscript witnesses; it is not itself an ancient autograph.

The project may say that a familiar church translation is a later edition and interpretation. It may not say that every difference was produced by a coordinated church rewrite.

## Four layers that must remain separate

| Layer | What changed | Evidence | On-card label |
|---|---|---|---|
| Historical tradition | Event, saying, or oral memory before a surviving Gospel | Multiple sources, context, external witnesses | `HISTORICAL TRADITION` |
| Gospel redaction | A Gospel author selects, adds, omits, reorders, or reframes inherited material | Literary comparison among Gospels | `GOSPEL_REDACTION` |
| Scribal variant | Later copies of the same passage preserve different wording | Named manuscript/version/patristic witnesses and apparatus | `SCRIBAL_VARIANT` |
| Translation history | A printed Greek edition or translation selects and renders a reading | Edition/translation preface, apparatus, and publication record | `TRANSLATION_HISTORY` |

Never place a Gospel-composition date and a medieval translation choice on one unlabeled line. Each timeline event carries its own category.

## Evidence hierarchy

1. Transcribe the passage from a named critical Greek edition.
2. Check the apparatus or a scholarly textual commentary for variants.
3. Name ancient witnesses only when the source supports the identification and date.
4. Compare Gospel tellings to identify authorial redaction; do not call this a manuscript variant.
5. Compare later editions/translations only after the ancient evidence is clear.
6. Mark disputed reconstructions as `DISPUTED`; never convert scholarly debate into certainty.

## Date language

- Gospel composition: `c. 65–75 CE`, never an invented exact year.
- Manuscript witness: `early 3rd century`, `mid-4th century`, or the catalogue's supported range.
- Printed edition/translation: exact publication year is allowed when verified.
- Unknown hand: `anonymous scribe/corrector`; do not assign motive without evidence.

## Change-track schema

```yaml
change_track:
  - date: "c. 65–75 CE"
    category: GOSPEL_REDACTION
    witness: "Mark 1:9"
    statement: "John is directly named as Jesus' baptizer; no objection is narrated."
    certainty: HIGH
  - date: "c. 80–95 CE"
    category: GOSPEL_REDACTION
    witness: "Matthew 3:14–15"
    statement: "The author adds John's objection and Jesus' reply."
    certainty: HIGH
```

Allowed `certainty` values: `HIGH`, `MODERATE`, `DISPUTED`.

## Honest wording patterns

Use:

- `The author of Matthew adds…`
- `This dialogue is absent from the earlier Markan account.`
- `Some ancient witnesses read…`
- `The earliest reading remains disputed.`
- `This translation follows reading A; its footnote records reading B.`

Do not use:

- `Matthew personally falsified…`
- `The church changed this in year X…` without a documented actor and event.
- `This is the untouched original.`
- `Four Gospels independently prove…` where literary dependence is likely.

## Required source basis

Each chapter README and portal entry must identify:

- critical Greek edition used;
- manuscript or apparatus basis for every textual variant;
- Gospel parallels used for redaction comparison;
- external source when used, such as Josephus;
- later translations/editions compared, with year;
- unresolved scholarly dispute.

