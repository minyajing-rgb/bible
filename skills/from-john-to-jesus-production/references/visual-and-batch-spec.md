# Visual and Batch Specification

## Card system

- 4:5 portrait PNG, matching `assets/approved-minimal-line-style.png`
- `assets/approved-minimal-line-style.png` is the binding style reference
- ultra-simple thin black ink doodle on an almost pure warm-white field
- compact, short-limbed, rounded adults; symbolic faces; dignified, never babyish
- tiny scene restricted to the lower-middle 25–33%; at least 70% negative space
- flat black hair/beard and plain garments drawn with very few lines
- exactly one low-saturation accent hue per card; it may be pale lavender, light gold, sky blue, coral, or green according to the scene
- no Chinese generated logo; deterministic English brand lock only
- simple black leaf-over-water brand mark at bottom center so it does not introduce a second accent hue

## Anti-drift prohibitions

Reject the image if any of these appear:

- watercolor, pencil shading, charcoal wash, gray modeling, cast shadows, or paper texture
- realistic anatomy, long limbs, cinematic lighting, painterly faces, or historical-concept-art rendering
- elaborate temple interiors, architecture, landscapes, fabric folds, furniture, or decorative props
- figures larger than roughly one third of the canvas height
- a second accent hue, gradient, border, frame, generated text, halo, or watermark
- any person or prop not required by the ledger beat

## Character lock

- John the Baptist as an adult: rough short camel-hair garment or coarse short tunic, leather belt, bare feet, forceful prophetic presence
- Zechariah: elderly, compact, gray beard, simple off-white priestly tunic
- Elizabeth: elderly, compact, dignified, layered off-white Judean dress and head covering
- Jesus does not appear before the roadmap reaches his entrance

## Ten-card mix

Target per batch:

- 4 action cards
- 2 public proclamation cards
- 2 relationship cards
- 1 quiet landscape/negative-space card
- 1 source-comparison card

Adapt the mix to what the source actually narrates. Never invent preaching or conflict merely to satisfy a quota. The source-comparison function may be carried by the deterministic note block on a narrative card.

## Typography lock

Each final card carries:

```text
GGC Spirituality Series · From John to Jesus

[LITERAL ENGLISH]
[English quotation]
[Book and verse]

[EARLIEST RECOVERABLE GREEK]
[Greek text]

[short scene caption]

SOURCE: [Book and verse]
SOURCE LAYER: [Source Layer]
DATE: [Approximate date]
PARALLEL: [Parallel passage or NONE]
HISTORICAL STATUS: [Status]
[REDACTION NOTE / TEXTUAL VARIANT / SOURCE CAUTION]: [Note]

[leaf-over-water mark]
GGC Spirituality Series
```

Keep the typography light, centered, and spacious like the approved reference. The six source lines must use explicit labels and remain readable at full size; do not collapse them into an unlabeled footer. Keep the illustration in a protected zone above the source block so lines and figures never cross the text. Use deterministic rendering for all words; image generation produces illustration only, and raw no-text assets are never user-facing deliverables.

## Typography QA gate

- Contact-sheet view: quotation, verse, and source-layer category are visually identifiable.
- Full-size view: Greek and all six labeled source fields are readable without zooming beyond 100%.
- No text crosses a figure, river line, mascot, logo, or another line of text.
- `SOURCE`, `SOURCE LAYER`, `DATE`, `PARALLEL`, and `HISTORICAL STATUS` appear literally on every card.
- The note line uses the ledger's exact label and wording.
