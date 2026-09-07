---
name: workshop-novel
description: Expand a novel chapter seed into a complete Workshop, Story, and Discussion draft while updating the chapter model with accurate word-count metadata.
---

# Novel Workshop

Use this skill for a novel pipeline after scaffold and before research or later filters.

## Inputs

Read, in order:

1. The pipeline model and cloned book plan:
   - .space/pipeline/<bookname>/model.json
   - .space/pipeline/<bookname>/book.json
2. The matching chapter model:
   - .space/pipeline/<bookname>/chapters/<n>/model.json
3. The current chapter draft:
   - .space/pipeline/<bookname>/chapters/<n>/chapter.md
4. The novel backlog source:
   - .space/backlog/epic/<bookname>/epic.md
   - .space/backlog/epic/<bookname>/gist.md
5. Any available upstream research and seed files in the pipeline.

The epic is the story source of truth. Use the gist only to orient the premise. Do not invent characters, events, history, or outcomes beyond the epic and available research.

## Draft Contract

Expand the current scaffolded draft into exactly these sections:

1. Workshop
2. Story
3. Discussion

Workshop is the modern frame that introduces the chapter question. Story is the continuous historical or fictional narrative drawn from the epic. Discussion is the frame's response and should create a meaningful handoff to the next chapter. Preserve the chapter title and canonical order. Do not use poetry-only sections.

## Word Target

Resolve the target from chapter model word_target first, then the matching book plan entry, then the pipeline model default. The target is authoritative.

Count words in the complete literary body of chapter.md, excluding Markdown headings. Expand or tighten the three sections until the count matches word_target as closely as possible; treat a result within 2 percent as acceptable unless the workflow specifies an exact count. Record the measured count in chapter model word_count and retain word_target. Never claim completion without measuring the draft.

## Metadata And Files

Before replacing a non-empty chapter.md, copy it into the chapter history folder with a timestamped or incrementing filename. Then write the enriched draft to the live chapter.md.

Merge into the existing chapter model without dropping unrelated fields:

- state: workshop
- workshop_skill: workshop-novel
- chapter_name and chapter_title
- chapter_summary
- word_target
- word_count
- workshop_file: chapters/<n>/chapter.md
- source_context: epic-and-research

Preserve chapter_index, level, segments, and all existing runtime fields.

Write one run summary to .space/pipeline/<bookname>/filters/workshop/filter-summary.md. Include the processed chapters, target and measured word counts, source grounding, and any unresolved research need. Do not write runtime content into other filter folders.

## Guardrails

- Work only in the named pipeline and its chapter history.
- Do not create or modify source/books.
- Do not run research, correctness, theme, syntax, override, or quality.
- Do not place writer output in segments/1/writer; that is a later stage.
- Preserve human-edited chapter content by archiving before replacement.
- The result must remain a prose narrative with a modern frame and continuous story.