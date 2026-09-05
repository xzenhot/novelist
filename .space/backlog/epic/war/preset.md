> **Note:** This preset was selected for `war` via `/write war configure [preset]` on 2026-09-05. It lives in the backlog and is read by `scaffold` to build the pipeline filter chain.

# Preset: simple_novel (adapted for 10 chapters)

Use 10 main chapters, one introductory chapter, and one conclusion chapter.
Use new story development for each chapter.
Use 4500 words as the target length for each main chapter unless the book pipeline overrides it.
Use the ordered steps below as the chapter-curation workflow; each step is an agent/filter applied to every selected chapter in sequence.

## Ordered filter chain

1. **workshop** — Create the three-section chapter frame: Workshop, Story, and Discussion, grounded in the epic and chapter plan.
2. **research** — Deepen and verify the chapter material, attaching era, place, figures, events, sources, and grounding notes.
3. **seeds** — Curate the chapter seed by selecting included characters, quality parameters, mood-shaped summary, and segment structure.
4. **correctness** — Check factual claims, names, dates, terms, and source traceability; record corrections and uncertainties.
5. **theme** — Assign the chapter theme, theme essence, contemporary mapping, and form-consistent stereotype selection.
6. **syntax** — Apply the selected syntax guidance so the chapter remains elevated, modern, readable, and ready for writing.
7. **override** — Human-in-the-loop gate: review, adjust, or override any prior filter output before writing begins.
8. **quality** — Final quality gate: verify completeness, consistency, register, and readiness for promotion.
