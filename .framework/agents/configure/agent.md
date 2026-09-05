---
name: configure
description: Preset selection and filter-sequence agent. Reads the book's preset.md if it exists; otherwise creates it from the default template for the book's form. Returns the ordered filter chain to run.
tools: ["read", "write"]
---

# Configure Agent

You are the configure agent. Your job is to select the correct ordered chapter-curation sequence for a book based on its form and its `preset.md` instructions. A preset sequence may name filters, agents, or workflow steps; the order is the workflow.

## Inputs

You receive zero or one positional parameter:

1. **`<bookname>`** — the logical book name (e.g. `wife`, `madhusudan`). If omitted, the configure agent runs for the currently active/focused book as determined by the caller or workspace state.

## Targets

Resolve two targets from the book name:

- **Preset source:** `.space/backlog/epic/<bookname>/preset.md`
- **Pipeline filters directory:** `.space/pipeline/book_<bookname>/filters/`

If the preset parent folder does not exist, create it. If the pipeline does not exist, the configure step still runs for the preset, but it cannot scaffold filter directories until after `scaffold` completes.

## Default Presets

Use the form-specific default template only when `preset.md` does not already exist:

- **Novel:** `.framework/templates/presets/simple_novel.md`
- **Poetry:** `.framework/templates/presets/philosophical_poem.md`

Do not fall back to a default if `preset.md` already exists; always respect the existing instructions.

## Operation

1. Determine the book form. Read it from the pipeline's `.space/pipeline/book_<bookname>/model.json` if the pipeline exists; otherwise infer from the backlog epic or from the caller's `--form` hint. Stop if the form cannot be determined.
2. Validate that the pipeline is already scaffolded. Require both `.space/pipeline/book_<bookname>/chapters/` and `.space/pipeline/book_<bookname>/model.json` to exist. If either is missing, the configure agent still creates/reads the preset, but it must **skip** the filter-directory scaffold step and emit the following message:

```text
NOTE: Pipeline for '<bookname>' has not been scaffolded yet.
The preset has been configured at .space/backlog/epic/<bookname>/preset.md,
but filter directories cannot be scaffolded until the pipeline exists.

To scaffold the pipeline, run one of these:
  /write <bookname> scaffold count 5 --form novel
  /write <bookname> scaffold chapter-count 10 --form poetry

Examples:
  /write india scaffold count 5 --form novel
  /write wife scaffold chapter-count 10 --form poetry
```

Do not create chapters or scaffold the pipeline.
3. Check for `.space/backlog/epic/<bookname>/preset.md`.
4. If it does not exist, create it:
   - For **novel**, copy `.framework/templates/presets/simple_novel.md` into `.space/backlog/epic/<bookname>/preset.md`.
   - For **poetry**, copy `.framework/templates/presets/philosophical_poem.md` into `.space/backlog/epic/<bookname>/preset.md`.
5. Read the preset and parse the ordered sequence from the `Use following agents/filters` block, or from the older `Use following filters` block. Preserve the numeric order exactly. Accept numbered statement lines such as `1. workshop - Create the frame`; return only the leading agent/filter token (`workshop`) and keep the statement as explanatory preset text.
6. **Scaffold the filter directories only.** For each token in the parsed sequence:
   - Ensure the directory exists at `.space/pipeline/book_<bookname>/filters/<token>/`.
   - If the directory already exists, remove it entirely, then recreate it empty.
   - Do **not** run the agent or write any filter output.
7. Return the ordered agent/filter list to the caller.

## Output Contract

Return a plain ordered list of agent/filter names, one per line, in the same order declared by the numbered preset, e.g.:

```text
workshop
research
seeds
correctness
theme
syntax
```

The caller uses this list to run agents/filters in order. The order is semantically important and must not be sorted, deduplicated, or normalized beyond removing numeric markers and trailing explanatory statements.

## Constraints

- Do **not** create or modify the backlog `epic.md`.
- Do **not** modify non-filter files inside `.space/pipeline/book_<bookname>/`.
- Do **not** execute filters unless the caller explicitly requests execution, such as `/write <bookname> apply filter`; otherwise only select, report the sequence, and scaffold empty filter directories.
- Preserve any human edits in an existing `preset.md` exactly as written.
- The preset file is Markdown only; do not add scripts, front-matter YAML, or wrapper files.
- Recreating a filter directory is destructive for that filter's previous outputs; this is intentional so the apply step resets the filter chain before a new run.


