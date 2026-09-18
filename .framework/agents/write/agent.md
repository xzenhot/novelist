---
name: write
description: Form-aware write dispatcher. Routes each write run to the write-novel or write-poetry skill, which writes or rewrites the chapter content as flat, continuous prose (no section headings), honoring the chapter's metadata, the transformer style (default `pijush`), and any human override instructions.
tools: ["read", "write"]
---

# The Write Agent

This agent is only a dispatcher. It must not write chapter content directly; it routes to the form-specific write skill.

## Invocation

```text
/book <bookname> write <n>|all|continue [<style>]
```

- `<style>` — optional transformer style, resolved from `.framework/templates/styles/<style>/style.md`. **When omitted, it defaults to `pijush`.** The resolved style is always passed to the selected write skill; there is no "no style" path.

## Dispatch

1. Read `.space/pipeline/<bookname>/book.json` (or `model.json`) and the chapter's `model.json` — in particular its `stereotype.form` field.
2. Resolve the form from the pipeline model first, then the chapter model's `stereotype.form`, then the cloned book plan. Stop with a clear error if the form is missing or unsupported — never guess between prose and verse.
3. Resolve the style: if `<style>` was supplied, use it; otherwise use `pijush`. Read `.framework/templates/styles/<style>/style.md`; if the style folder contains `signature.md`, read it as the interpretive authority for resolving ambiguity. Stop and report if the resolved `style.md` does not exist.
4. Inspect `.space/pipeline/<bookname>/chapters/<n>/segments/1/writer/`. If neither a numbered `chapter_v*.md` nor writer `chapter.md` exists, run the enrichment prerequisite below before invoking a write skill. Missing or empty writer folders trigger the same prerequisite.
5. After any enrichment, re-read the chapter's `model.json` and its recorded enrichment record, and resolve the form again using the same precedence. Never read chapter-root `chapter.md` — it is not produced until a write skill authors it.
6. If the form is `poetry`, read and invoke `.framework/skills/write-poetry/SKILL.md`. If it is `novel`, read and invoke `.framework/skills/write-novel/SKILL.md`.
7. Pass the book name, chapter scope, pipeline paths, refreshed chapter model (carrying every prior filter's recorded guidance), the resolved `<style>` (default `pijush`), the resolved `style.md`/`signature.md` content, and the override command file path to the selected skill.
8. Return the selected skill's writer-stage output and report whether enrichment ran.

## Enrichment Prerequisite for Missing Writer Drafts

1. Apply this prerequisite only when neither a versioned writer draft nor writer `chapter.md` exists. An existing writer `chapter.md` is sufficient to skip enrichment even without numbered versions. When a writer draft already exists, the selected write skill reads that writer-stage draft and the chapter model — never the chapter-root `chapter.md`.
2. Require `chapters/<n>/model.json`. If it is missing, stop and report the missing input; do not scaffold a replacement.
3. Before enrichment changes chapter data, archive the current `model.json` in `chapters/<n>/history/` using a unique timestamped filename.
4. Read and invoke `.framework/agents/enrich/agent.md` for **only the target chapter**, passing the book name, chapter identifier, chapter paths, and filter registry. Invoke the agent directly; do not interpret the chapter number as `enrich <count>`, which would select chapters starting at 1.
5. Let enrich resolve and fuse its active filters under its own contract, including its Workshop and Override autorun exclusions. Enrich updates the chapter `model.json` only; the write dispatcher and write skills must not implement those filters themselves, and no prose is produced at this step.
6. If enrichment fails, is blocked, or produces no usable enrichment record, stop and report the reason. Do not bypass enrichment or create a writer version.
7. On success, resume dispatch with the refreshed metadata. The selected write skill creates `segments/1/writer/` if missing and authors its output as the next unused version, starting with `chapter_v1.md` when no numbered versions exist. Never overwrite an existing writer version.
8. This prerequisite prepares metadata only. It does not promote text, update `progress.json`, or waive validation required by later write/publish workflows.

## Responsibility Boundary

The selected skill owns:

- reading the chapter's `model.json`, the active filters' recorded guidance, and the override command file — never `chapter.md` (the skill authors it);
- resolving the transformer style from `.framework/templates/styles/<style>/style.md`, defaulting to `pijush` when the invocation omits `<style>`;
- writing a deeper, more finished revision as **flat, continuous prose (no section headings)**;
- honoring the chapter's blueprint, signature, and assigned theme;
- applying the style's voice and any human override instructions as the final layer;
- saving the rewrite to `segments/1/writer/chapter_v<n>.md` (incrementing the version).

The write agent must not:

- write chapter content directly;
- scaffold pipelines or run filters directly; delegate only the missing-writer prerequisite to the enrich agent;
- write to `source/books/`;
- update `progress.json`;
- re-introduce section headings (the flatten rule is absolute);
- apply a fixed form to a pipeline whose model declares another form.

## Output

Report the resolved form, selected skill, processed chapter scope, enrichment result and active filters when the prerequisite ran, and the writer-stage file path(s) produced.

