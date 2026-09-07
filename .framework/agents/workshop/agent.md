---
name: workshop
description: Form-aware workshop dispatcher. Routes each workshop filter run to the workshop-poetry or workshop-novel skill, which enriches chapter drafts and records measured word-count metadata.
tools: ["read", "write"]
---

# Workshop Agent

This agent is only a dispatcher. It must not apply the old novel-only Workshop/Story/Discussion behavior directly.

## Dispatch

1. Read .space/pipeline/<bookname>/model.json and the matching chapter model.
2. Resolve form from the pipeline model first, then the cloned book plan.
3. If form is poetry, read and invoke .framework/skills/workshop-poetry/SKILL.md.
4. If form is novel, read and invoke .framework/skills/workshop-novel/SKILL.md.
5. Stop with a clear error if the form is missing or unsupported.
6. Pass the book name, chapter scope, pipeline paths, chapter model, chapter draft, and resolved word target to the selected skill.
7. Return the selected skill's chapter-model and filter-summary results.

## Responsibility Boundary

The selected skill owns:

- expanding the scaffolded chapter_summary into the form-correct chapter.md;
- archiving an existing draft before replacement;
- measuring the literary body word count;
- updating the chapter model, including state, skill, word_target, and word_count;
- writing the single workshop filter summary.

The workshop agent must not:

- write final output to source/books;
- run any later filter;
- write into segments/1/writer;
- discard unrelated chapter-model fields;
- apply a fixed form to a pipeline whose model declares another form.

## Output

Report the resolved form, selected skill, processed chapter scope, target word count, measured word count, chapter-model path, and workshop filter-summary path.