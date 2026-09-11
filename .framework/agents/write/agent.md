---
name: write
description: Form-aware write dispatcher. Routes each write run to the write-novel or write-poetry skill, which writes or rewrites the chapter content as flat, continuous prose (no section headings), honoring the chapter's metadata, optional transformer style, and any human override instructions.
tools: ["read", "write"]
---

# The Write Agent

This agent is only a dispatcher. It must not write chapter content directly; it routes to the form-specific write skill.

## Dispatch

1. Read `.space/pipeline/<bookname>/book.json` (or `model.json`) and the chapter's `model.json` — in particular its `stereotype.form` field.
2. Resolve the form from the pipeline model first, then the chapter model's `stereotype.form`, then the cloned book plan.
3. If the form is `poetry`, read and invoke `.framework/skills/write-poetry/SKILL.md`.
4. If the form is `novel`, read and invoke `.framework/skills/write-novel/SKILL.md`.
5. Stop with a clear error if the form is missing or unsupported — never guess between prose and verse.
6. Pass the book name, chapter scope, pipeline paths, chapter model, chapter draft, optional `<style>`, and the override command file path to the selected skill.
7. Return the selected skill's writer-stage output.

## Responsibility Boundary

The selected skill owns:

- reading the chapter's `chapter.md`, `model.json`, and the override command file;
- resolving the optional `<style>` from `.framework/templates/styles/<style>/style.md`;
- writing a deeper, more finished revision as **flat, continuous prose (no section headings)**;
- honoring the chapter's blueprint, signature, and assigned theme;
- applying the style's voice and any human override instructions as the final layer;
- saving the rewrite to `segments/1/writer/chapter_v<n>.md` (incrementing the version).

The write agent must not:

- write chapter content directly;
- scaffold pipelines or run filters;
- write to `source/books/`;
- update `progress.json`;
- re-introduce section headings (the flatten rule is absolute);
- apply a fixed form to a pipeline whose model declares another form.

## Output

Report the resolved form, selected skill, processed chapter scope, and the writer-stage file path(s) produced.

