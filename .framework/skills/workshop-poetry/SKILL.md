---
name: workshop-poetry
description: Expand a poetry chapter seed into a complete Question, Oration, and Benediction draft while updating the chapter model with accurate word-count metadata.
---

# Poetry Workshop

Use this skill for a poetry pipeline after scaffold and before research or later filters.

## Inputs

Read, in order:

1. The pipeline model and cloned book plan:
   - .space/pipeline/<bookname>/model.json
   - .space/pipeline/<bookname>/book.json
2. The matching chapter model:
   - .space/pipeline/<bookname>/chapters/<n>/model.json
3. The current chapter draft:
   - .space/pipeline/<bookname>/chapters/<n>/chapter.md
4. The backlog sources:
   - .space/backlog/epic/<bookname>/gist.md
   - .space/backlog/epic/<bookname>/epic.md

The chapter_summary is the seed, not the finished work. Use the gist and epic only for contextual grounding. Do not invent historical claims, figures, events, or sources that are absent from those inputs.

## Draft Contract

Expand the current scaffolded draft into exactly these sections:

1. Question
2. Oration
3. Benediction

Keep the chapter title and topic. The Question should establish the chapter's central tension. The Oration should carry the substantive image, context, movement, and reflection. The Benediction should close with an earned consequence, opening, or responsibility. Do not add novel-only sections and do not force a signature or subject that the chapter metadata does not support.

## Word Target

Resolve the target from chapter model word_target first, then the matching book plan entry, then the pipeline model default. The target is authoritative.

Count words in the complete literary body of chapter.md, excluding Markdown headings. Expand or tighten the three sections until the count matches word_target as closely as possible; treat a result within 2 percent as acceptable unless the workflow specifies an exact count. Record the measured count in chapter model word_count and retain word_target. Never claim completion without measuring the draft.

## Metadata And Files

Before replacing a non-empty chapter.md, copy it into the chapter history folder with a timestamped or incrementing filename. Then write the enriched draft to the live chapter.md.

Merge into the existing chapter model without dropping unrelated fields:

- state: workshop
- workshop_skill: workshop-poetry
- chapter_name and chapter_title
- topic
- chapter_summary
- word_target
- word_count
- workshop_file: chapters/<n>/chapter.md
- source_context: gist-and-epic

Preserve chapter_index, level, segments, and all existing runtime fields.

Write one run summary to .space/pipeline/<bookname>/filters/workshop/filter-summary.md. Include the processed chapters, target and measured word counts, and any grounding limitation. Do not write runtime content into other filter folders.

## Guardrails

- Work only in the named pipeline and its chapter history.
- Do not create or modify source/books.
- Do not run research, correctness, theme, syntax, override, or quality.
- Do not place writer output in segments/1/writer; that is a later stage.
- Preserve human-edited chapter content by archiving before replacement.
- The result must remain a poetry draft even when the book's subject is historical, political, ecological, or philosophical.