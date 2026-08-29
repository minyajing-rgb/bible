# Chapter Template and Samples

## Required chapter brief

```yaml
chapter_id:
part:
batch_id:
title:
shared_entry_point:
central_evidence_question:
one_sentence_claim:
critical_greek_edition:
source_spine:
source_layers_compared:
manuscript_variants:
translations_compared:
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
    greek:
    literal_english:
    source:
    source_layer:
    critical_text_basis:
    scene_action:
    evidence_status:
    change_track:
      - date:
        category:
        witness:
        statement:
        certainty:
```

The one-sentence claim is the chapter's evidence contract. Every card must advance, qualify, test, or conclude it.

## Card functions

- `ORIENTATION`
- `ACTION`
- `PROCLAMATION`
- `RELATIONSHIP`
- `CONSEQUENCE`
- `SOURCE_COMPARISON`
- `TEXTUAL_VARIANT`
- `TRANSLATION_COMPARISON`
- `CHAPTER_CONCLUSION`

Analytical text is never presented as ancient dialogue.

# Sample A · Chapter 12 · Mark 1:9

## Chapter claim

> The earliest extant complete Gospel account directly names John as Jesus' baptizer; Matthew later adds an objection and reply, Luke reports the baptism passively, and John reframes it as remembered witness.

## Sample card record

```yaml
card_id: CH12-02
function: ACTION
event_or_analysis: "John directly baptizes Jesus in the Jordan."
speaker: Narrator
quote_type: NARRATION
greek: "ἐβαπτίσθη εἰς τὸν Ἰορδάνην ὑπὸ Ἰωάννου"
literal_english: "He was baptized into the Jordan by John."
source: "Mark 1:9"
source_layer: "EARLIEST EXTANT NARRATIVE"
composition_date: "c. 65–75 CE"
critical_text_basis: "SBLGNT; compare NA28/ECM apparatus where available"
scene_action: "Small lower-middle river scene: John supports Jesus in the water."
evidence_status: "Mark directly names John; no objection is narrated."
change_track:
  - date: "c. 65–75 CE"
    category: GOSPEL_REDACTION
    witness: "Mark 1:9"
    statement: "John is directly named as baptizer; no dialogue explains the act."
    certainty: HIGH
  - date: "c. 80–95 CE"
    category: GOSPEL_REDACTION
    witness: "Matthew 3:14–15"
    statement: "The author adds John's objection and Jesus' answer."
    certainty: HIGH
  - date: "c. 80–95 CE"
    category: GOSPEL_REDACTION
    witness: "Luke 3:21"
    statement: "The baptism is reported passively; the baptizer is unnamed in the scene."
    certainty: HIGH
  - date: "c. 90–100 CE"
    category: GOSPEL_REDACTION
    witness: "John 1:32–34"
    statement: "The immersion is not narrated; John recalls seeing the Spirit descend and remain."
    certainty: HIGH
```

This is a Gospel-redaction timeline, not a scribal-variant timeline. Do not say that a later copyist removed Matthew's dialogue from Mark.

# Sample B · Luke 3:22 · actual textual variant

```yaml
card_id: CH04-VAR
function: TEXTUAL_VARIANT
speaker: Heavenly voice in the narrative
source: "Luke 3:22"
critical_text_reading:
  greek: "Σὺ εἶ ὁ υἱός μου ὁ ἀγαπητός, ἐν σοὶ εὐδόκησα."
  literal_english: "You are my Son, the beloved; in you I was well pleased."
alternative_reading:
  greek: "Υἱός μου εἶ σύ, ἐγὼ σήμερον γεγέννηκά σε."
  literal_english: "You are my Son; today I have begotten you."
evidence_status: "The main modern critical text prints the first reading; the Psalm 2:7 reading survives in an important ancient stream and its priority is disputed."
change_track:
  - date: "2nd–5th centuries"
    category: SCRIBAL_VARIANT
    witness: "Old Latin/patristic witnesses; Codex Bezae in Greek"
    statement: "An alternative voice quotes Psalm 2:7: ‘today I have begotten you.’"
    certainty: DISPUTED
  - date: "modern critical editions"
    category: TRANSLATION_HISTORY
    witness: "NA28 / most modern translations"
    statement: "The beloved/well-pleased reading is printed; the alternative is commonly footnoted."
    certainty: HIGH
```

Do not claim a known individual or council made this change. The witnesses preserve different readings; motive and priority remain debated.

## Sample rejection

Reject a Mark 1:9 card that quotes “I need to be baptized by you” as Markan dialogue. It belongs to Matthew 3:14. Reject a Luke 3:22 card that labels the Psalm 2:7 reading `MATTHEAN REDACTION`; it is a manuscript/textual variant within Luke's transmission.

