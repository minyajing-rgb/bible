# Chapter Template and Sample

## Required chapter brief

```yaml
chapter_id:
part:
batch_id:
title:
narrative_function:
central_question:
one_sentence_claim:
source_spine:
source_layers_compared:
excluded_material:
opening_state:
ending_state:
bridge_to_next_chapter:
ten_card_map:
  - card_id:
    function:
    event_or_analysis:
    speaker:
    quote_type:
    text_unit:
    greek:
    source:
    source_layer:
    source_note:
    visual_action:
```

The `one_sentence_claim` is the chapter's editorial contract. All ten cards must advance, test, qualify, or conclude that claim.

## Card-function vocabulary

- `ORIENTATION` — establishes place, time, actor, or source layer
- `ACTION` — shows a sourced physical event
- `PROCLAMATION` — presents sourced public speech
- `RELATIONSHIP` — shows a sourced interaction or handover
- `CONSEQUENCE` — shows what changes because of the preceding event
- `SOURCE_COMPARISON` — compares accounts without impersonating ancient speech
- `CHAPTER_CONCLUSION` — states the evidence-bounded result and bridge

`SOURCE_COMPARISON` and `CHAPTER_CONCLUSION` use `quote_type: SOURCE_ANALYSIS`. Their text is never placed in quotation marks.

# Full Sample · Chapter 08

## Chapter brief

```yaml
chapter_id: CH-08
part: II · THE WATER
batch_id: S02-B08
title: "Mark: Earliest Extant Baptism Narrative"
narrative_function: "Show the earliest surviving complete baptism account before later Gospel explanations are introduced."
central_question: "What does the earliest extant narrative actually say happened at the Jordan?"
one_sentence_claim: "Mark directly names John as Jesus' baptizer, narrates no objection, and centers the torn heavens, descending Spirit, and voice addressed to Jesus."
source_spine: "Mark 1:9–11 · c. 65–75 CE"
source_layers_compared:
  - "Matthew 3:13–17 · later objection and reply"
  - "Luke 3:21–22 · passive baptism report; baptizer unnamed in scene"
  - "John 1:32–34 · immersion not narrated; event reframed as witness"
excluded_material:
  - "Matthew's objection inside the Markan action sequence"
  - "Luke's prayer emphasis presented as Markan narration"
  - "Fourth-Gospel Lamb-of-God language presented as Markan speech"
opening_state: "Jesus arrives from Nazareth at John's Jordan movement."
ending_state: "The earliest account is visible on its own, and the reader is ready to examine Matthew's later explanation."
bridge_to_next_chapter: "Chapter 09 asks why the author of Matthew adds John's resistance and Jesus' answer."
```

## Ten-card map

| Card | Function | Text unit | Source / layer | Visual action | Required note |
|---:|---|---|---|---|---|
| 01 | ORIENTATION | “Jesus came from Nazareth of Galilee.” | Mark 1:9 · earliest extant narrative | Jesus approaches the Jordan | Mark moves directly from John's proclamation to Jesus' arrival. |
| 02 | ACTION | “He was baptized in the Jordan by John.” | Mark 1:9 · earliest extant narrative | John and Jesus enter the water | Mark explicitly names John as baptizer. |
| 03 | ACTION | “Immediately, coming up out of the water…” | Mark 1:10 · earliest extant narrative | Jesus rises from the river | Do not add Matthew's dialogue. |
| 04 | ACTION | “He saw the heavens being torn open.” | Mark 1:10 · earliest extant narrative | A single opening line above Jesus | Mark uses `σχιζομένους`, a forceful “being torn.” |
| 05 | ACTION | “The Spirit descending into him like a dove.” | Mark 1:10 · earliest extant narrative | Dove-form descends; one blue accent | Record the Greek preposition and translation choice. |
| 06 | CONSEQUENCE | “A voice came from the heavens.” | Mark 1:11 · narration | John and Jesus listen; no invented speaker figure | The voice is narrated, not visually personified. |
| 07 | RELATIONSHIP | “You are my beloved Son.” | Mark 1:11 · direct heavenly voice | Jesus remains central; John witnesses nearby | In Mark the address is second person, directed to Jesus. |
| 08 | CONSEQUENCE | “In you I am well pleased.” | Mark 1:11 · direct heavenly voice | Quiet water after the declaration | Keep Luke 3:22's textual variant for Luke's own chapter. |
| 09 | SOURCE_COMPARISON | `MARK: John named · no objection narrated` | Mark compared with Matthew, Luke, John | Four-column source diagram, no invented event | Label later additions/reframings; do not call them scribal changes. |
| 10 | CHAPTER_CONCLUSION | `EARLIEST EXTANT NARRATIVE: John directly baptizes Jesus.` | Source analysis | Empty Jordan path turning toward Chapter 09 | Bridge: Matthew later adds objection and reply. |

## Sample card record · Card 02

```yaml
card_id: CH08-02
function: ACTION
event_or_analysis: "John directly baptizes Jesus in the Jordan."
speaker: Narrator
quote_type: NARRATION
text_unit: "He was baptized in the Jordan by John."
greek: "ἐβαπτίσθη εἰς τὸν Ἰορδάνην ὑπὸ Ἰωάννου"
source: "Mark 1:9"
source_layer: "EARLIEST EXTANT NARRATIVE"
date: "c. 65–75 CE"
parallel: "Matthew 3:13–17 · Luke 3:21–22 · John 1:32–34"
historical_status: "Core historical tradition with later narrative reframing"
source_note: "Mark names John as the baptizer and narrates no objection."
visual_action: "Tiny lower-middle Jordan scene; John supports Jesus during immersion; one pale-blue water accent; at least 70% negative space."
```

## Sample rejection

Reject a Chapter 08 card that shows John saying “I need to be baptized by you” while labeling the source `Mark 1:9`. The sentence belongs to Matthew 3:14 and is a Matthean addition to the earlier Markan scene. Either move it to Chapter 09 or label it as a source comparison rather than Markan dialogue.
