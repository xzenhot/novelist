> **Note:** This preset was selected for `aravalli` via `/write aravalli configure poetry` on 2026-09-05. It lives in the backlog and is read by `scaffold` to build the pipeline filter chain.

# Preset: philosophical_poem (adapted for 10 chapters)

Use 10 main poems, one introductory poem, and one conclusion poem.
Use new poetic development for each chapter.
Use 500 words as the target length for each poem unless the book pipeline overrides it.
Use the ordered steps below as the chapter-curation workflow; each step is an agent/filter applied to every selected poem in sequence.

Use following agents/filters in this exact numbered order:

1. research - Gather and organize the subject, context, source notes, and usable images for the poem.
2. correctness - Verify factual, attributional, religious, philosophical, and cultural claims before poetic rendering.
3. theme - Assign the poem's philosophical lens, contemporary mapping, and form-consistent poetic stereotype selection.
4. syntax - Apply the selected poetic syntax guidance so the language remains current while preserving elevated cadence.
5. override - Apply any human transformation instructions from the override layer, or pass through unchanged when empty.
6. quality - Audit the poem against the preset, topic, theme, voice, correctness result, and final quality bar.