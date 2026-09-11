---
name: workshop-poetry
description: Expand a poetry chapter seed into a complete flat, continuous poetic-prose draft while updating the chapter model with accurate word-count metadata.
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

The chapter_summary is the seed, not the finished work. The epic is the primary source of truth: extend every chapter from the epic's premise, setting, thematic threads, topical structure, and world-building, so each poem is grounded in the book's full narrative foundation rather than the one-line seed alone. Use the gist for the high concept and the epic for the concrete material. Do not invent historical claims, figures, events, or sources that are absent from those inputs.

## Story Requirement

Every chapter must carry at least a basic story, not a bare meditation. A story means a concrete movement: a speaker or figure in a specific place and time, an event or image that happens, a turn or change, and a consequence that lands. Ground the story in the epic's topical structure and world-building — the ridge, the vanished river, the volcanic fire, the dynasties, the woman who is Delhi — so each poem reads as a scene with a beginning, a middle, and an end, not a list of abstractions. This story-bearing draft is the foundation that later filters (research, correctness, theme, syntax, override, quality) will refine into publish-ready verse, so it must be substantial and self-contained enough to survive that chain.

## Draft Contract

Expand the current scaffolded draft into **flat, continuous poetic prose** — no section headings. The `## Question`, `## Oration`, and `## Benediction` headings are removed entirely; only the prose that followed them remains, merged into continuous paragraphs. The only heading permitted is the chapter title (`# {chapter_title}`). Do not leave empty headings, stray `#` markers, or orphaned labels.

Keep the chapter title and topic. The prose should open with the chapter's central tension, carry the substantive image, context, movement, and reflection, and close with an earned consequence, opening, or responsibility. Do not add novel-only sections and do not force a signature or subject that the chapter metadata does not support.

The prose must advance a story drawn from the epic: it names a concrete scene or figure and its tension, enacts an event, image, or turn grounded in the epic's setting and world-building, and delivers the consequence of that turn. A chapter that only restates the summary or lists abstractions is incomplete and must be expanded until it carries a basic story.

## Word Target

Resolve the target from chapter model word_target first, then the matching book plan entry, then the pipeline model default. The target is authoritative.

Count words in the complete literary body of chapter.md, excluding Markdown headings. Expand or tighten the prose until the count matches word_target as closely as possible; treat a result within 2 percent as acceptable unless the workflow specifies an exact count. Record the measured count in chapter model word_count and retain word_target. Never claim completion without measuring the draft.

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

## Epic Grounding

Before expanding a chapter, read `.space/backlog/epic/<bookname>/epic.md` in full and locate the material that belongs to this chapter: its entry in the topical structure, the relevant thematic threads, and the world-building images that fit the chapter's subject. Extend the chapter from that material so the poem is recognizably part of the book's larger narrative arc. If the epic has no direct entry for a chapter, derive the story from the epic's premise, setting, and recurring images rather than from the seed alone. The resulting draft must be substantial enough to serve as the input for the full filter chain (research, correctness, theme, syntax, override, quality) that prepares it for publish.

Write one run summary to .space/pipeline/<bookname>/filters/workshop/filter-summary.md. Include the processed chapters, target and measured word counts, and any grounding limitation. Do not write runtime content into other filter folders.

## Guardrails

- Work only in the named pipeline and its chapter history.
- Do not create or modify source/books.
- Do not run research, correctness, theme, syntax, override, or quality.
- Do not place writer output in segments/1/writer; that is a later stage.
- Preserve human-edited chapter content by archiving before replacement.
- The result must remain a poetry draft even when the book's subject is historical, political, ecological, or philosophical.