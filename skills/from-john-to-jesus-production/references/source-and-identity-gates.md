# Source and Identity Gates

## Source Gate

- Record book, verse, speaker, quotation type, Greek text, literal English, source layer, approximate date, parallels, and historical status.
- Treat Mark as the earliest extant full narrative spine, ordinarily dated c. 65–75 CE.
- Treat Matthew and Luke as later Synoptic works that use Mark plus other material; three Synoptic appearances are not automatically three independent votes.
- Treat the Fourth Gospel's John-the-Baptist material as a later Johannine witness layer unless a specific saying has earlier independent support.
- Treat Q as a scholarly reconstruction, not a discovered manuscript.
- For Josephus, distinguish his political-crowd explanation from the Gospel marriage/banquet account.

## Identity Gate

Allowed value in this series:

```text
JOHN_BAPTIST
```

Rejected identities:

```text
JOHN_ZEBEDEE
BELOVED_DISCIPLE
JOHANNINE_AUTHOR
```

## Quote Gate

Allowed `quote_type` values:

```text
DIRECT_JESUS
DIRECT_JOHN_BAPTIST
DIRECT_OTHER
NARRATION
EXTERNAL_SOURCE
```

Never turn narrative prose into spoken dialogue. A concise excerpt may be used, but its speaker/type must remain accurate.

## Transmission Gate

Use “earliest recoverable Greek text,” not “unaltered original.” Distinguish:

- historical tradition
- authorial redaction
- scribal variant
- later interpretation

For a variant, present the concrete readings and witnesses/critical-text status. Do not invent a secret editor or council.

