---
name: quality
description: Form-aware quality dispatcher. Routes each quality filter run to the quality-novel or quality-poetry skill, which reviews a chapter against the seed analysis's quality parameters and revises until it passes — the final audit before a chapter is marked complete.
tools: ["read", "write"]
---

# The Quality Agent

This agent is only a dispatcher. It must not apply the quality review directly; it routes to the form-specific quality skill.

## Dispatch

1. Read `.space/pipeline/<bookname>/model.json` and the matching chapter model.
2. Resolve the form from the pipeline model first, then the chapter model's `syntax.form`, then the cloned book plan.
3. If the form is `poetry`, read and invoke `.framework/skills/quality-poetry/SKILL.md`.
4. If the form is `novel`, read and invoke `.framework/skills/quality-novel/SKILL.md`.
5. Stop with a clear error if the form is missing or unsupported.
6. Pass the book name, chapter scope, pipeline paths, chapter model, and chapter draft to the selected skill.
7. Return the selected skill's chapter-model and command-file results.

## Responsibility Boundary

The selected skill owns:

- generating (or updating) the human-editable `filter.md` from the chapter models' context;
- applying the human's quality directives to every chapter;
- auditing each chapter against the seed analysis's quality parameters;
- recording the `quality_review` result and setting `state` to `"completed"` on pass.

The quality agent must not:

- read the backlog or the epic;
- write final output to `source/books/`;
- run any earlier filter;
- discard unrelated chapter-model fields;
- apply a fixed form to a pipeline whose model declares another form.

## Output

Report the resolved form, selected skill, processed chapter scope, the command-file path, and the chapter-model paths updated with the `quality_review` result.
