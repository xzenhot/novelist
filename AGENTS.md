# AGENTS.md

Universal runtime steering for autonomous coding agents operating in this repository. This document is intentionally self-contained and uses only repository-native markdown instructions. Do not add scripts, wrappers, aliases, shell helpers, or generated command shims to interpret it.

## Runtime Contract

This repository is an autonomous literary workflow system. Agent engines such as Claude Code, GitHub Copilot CLI, Kiro, and Codex must treat this file as the root steering document, then delegate detailed workflow behavior to the framework files under `.framework/`.

The primary command surface is:

```text
/write [args...]
```

When a user invokes `/write`, parse the arguments, inspect the current repository state, then execute the matching workflow defined in:

```text
.framework/workflows/write.md
```

`write.md` is the primary orchestration specification for command syntax, book lifecycle, filter order, progress tracking, form handling, and output promotion.

## Strict Slash Command Protocol

All `/write` commands must be interpreted from left to right. Preserve user-provided argument text exactly unless the workflow explicitly normalizes it.

Supported command families are defined by `.framework/workflows/write.md`. At minimum, the runtime must recognize these shapes:

```text
/write <bookname>
/write <bookname> gist [<gist>]
/write <bookname> scaffold <gist> count|chapter-count <number> [--form novel|poetry]
/write <bookname> add <chapter-count> filter <filter>|*|all
/write <bookname> filter <filter>|*|all
/write <bookname> chapter <chapter>|<n>|all|continue
/write <bookname> form <novel|poetry>
/write <bookname> config [<key> [<value>]]
/write -o | --options
/write -h | --help
```

Do not invent alternate slash commands. Do not treat subcommand keywords as book names, chapter names, filters, or prose.

## Parameter Parsing

When parsing `/write [args...]`, classify parameters into these slots.

### Target Work Or Book

The first positional argument after `/write` is normally `<bookname>`.

Map it to repository paths as follows:

```text
<bookname>                       -> logical book name, e.g. wife
.space/backlog/epic/<bookname>/  -> backlog epic folder
.space/pipeline/book_<bookname>/ -> pipeline folder
source/books/book_<bookname>/    -> final book output folder
```

If the user supplies `book_wife`, treat the canonical `<bookname>` as `wife` unless an existing path proves otherwise. Prefer existing repository paths over inference.

### Unit, Chapter, And Segment

A chapter/unit argument may be:

```text
Introduction
Conclusion
<n>
all
continue
<topic-name>
```

A segment may be expressed as:

```text
<chapter>/<segment>
1/1
Introduction/1
Conclusion/1
```

Map chapter and segment paths to:

```text
.space/pipeline/book_<bookname>/chapters/<chapter>/
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/
```

For poetry, every chapter has exactly one segment:

```text
segments/1
```

Do not create chapter folders outside `chapters/`. Do not create segment folders outside `chapters/<chapter>/segments/`.

### Signature Or Author Persona

A signature/persona argument selects an authorial voice. Resolve it from the form-specific stereotype folders:

```text
.framework/templates/stereotypes/novel/signatures/<signature>/signature.md
.framework/templates/stereotypes/poetry/signatures/<signature>/signature.md
```

Known novel signatures include:

```text
aurilus, bankim, bibhutibhushan, dostoevsky, faulkner, gibran, hemingway,
jibanananda, joyce, kafka, mahasweta, manik, marquez, morrison, mujtaba,
proust, rabindrasangeet, sarat, sunil, tarashankar, tolstoy, woolf
```

Known poetry signatures include:

```text
aurilus, blake, dickinson, eliot, gibran, hafez, jibanananda, lorca,
nazrul, neruda, rabindranath, rabindrasangeet, rilke, rumi, shakti,
sukanta, whitman, yeats
```

Read the relevant `registry.md` before using a signature when the workflow requires discovery or validation.

### Stage Or Role

A stage/role argument identifies the pipeline actor responsible for a unit of work:

```text
writer
editor
translator
```

Segment-stage paths are:

```text
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/writer/
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/editor/
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/translator/
```

Filter-stage roles are implemented by agents under:

```text
.framework/agents/<filter>/agent.md
```

Known filter agents:

```text
correctness, scaffold, override, poet, quality, reframe, research,
seeds, syntax, theme, workshop
```

Known post-scaffold agents:

```text
postlayout
```

Known pre-scaffold agents:

```text
prelayout
```

## Agent-First Skill Invocation

Workflows must never execute skills directly.

All skill-backed work must route through an agent:

```text
.framework/agents/<agent-name>/agent.md
```

The agent may then read and apply the corresponding skill:

```text
.framework/skills/<skill-name>/SKILL.md
```

If a required agent is missing, create `.framework/agents/<agent-name>/agent.md` first, then use that agent to invoke the skill. Do not bypass this rule for layout, research, filters, writing, editing, translation, or validation.

Scaffold/layout work is always mediated by:

```text
.framework/agents/scaffold/agent.md
```

The scaffold agent dispatches to:

```text
.framework/skills/layout-novel/SKILL.md
.framework/skills/layout-poetry/SKILL.md
```

## Framework Source Map

Use these framework locations as authoritative inputs.

### Workflow

```text
.framework/workflows/write.md
```

Primary orchestration spec for `/write`.

### Agents

```text
.framework/agents/correctness/agent.md
.framework/agents/scaffold/agent.md
.framework/agents/prelayout/agent.md
.framework/agents/postlayout/agent.md
.framework/agents/override/agent.md
.framework/agents/poet/agent.md
.framework/agents/quality/agent.md
.framework/agents/reframe/agent.md
.framework/agents/research/agent.md
.framework/agents/seeds/agent.md
.framework/agents/syntax/agent.md
.framework/agents/theme/agent.md
.framework/agents/workshop/agent.md
```

Agents are the only valid runtime entry points for skill-backed behavior.

### Skills

```text
.framework/skills/contemporary/SKILL.md
.framework/skills/correctness/SKILL.md
.framework/skills/dialogue/SKILL.md
.framework/skills/geography/SKILL.md
.framework/skills/history/SKILL.md
.framework/skills/indian/SKILL.md
.framework/skills/layout/SKILL.md
.framework/skills/layout-novel/SKILL.md
.framework/skills/layout-poetry/SKILL.md
.framework/skills/mythology/SKILL.md
.framework/skills/narrative/SKILL.md
.framework/skills/pacing/SKILL.md
.framework/skills/philosophy/SKILL.md
.framework/skills/poeticprose/SKILL.md
.framework/skills/quality/SKILL.md
.framework/skills/research/SKILL.md
.framework/skills/revision/SKILL.md
.framework/skills/syntax/SKILL.md
.framework/skills/theme/SKILL.md
.framework/skills/translation/SKILL.md
```

Read skill files only from inside the responsible agent flow.

### Rules And Templates

```text
.framework/rules/
.framework/templates/moods/
.framework/templates/presets/
.framework/templates/stereotypes/novel/
.framework/templates/stereotypes/poetry/
.framework/templates/subjects/
```

Use templates as source material; do not copy whole template trees into pipelines unless a scaffold agent explicitly requires it.

## Data And Output Path Map

### Backlog Source

Novel backlog epics live at:

```text
.space/backlog/epic/<bookname>/epic.md
```

For novels, `epic.md` is the story source of truth. Do not invent story content beyond it.

### Pipeline Working State

Book pipelines live at:

```text
.space/pipeline/book_<bookname>/
```

Common pipeline files:

```text
.space/pipeline/book_<bookname>/model.json
.space/pipeline/book_<bookname>/book.json
.space/pipeline/book_<bookname>/characters.json
.space/pipeline/book_<bookname>/bookseed.txt
.space/pipeline/book_<bookname>/progress.json
.space/pipeline/book_<bookname>/filters/
.space/pipeline/book_<bookname>/chapters/
```

Novel pipelines use `epic.md`, `book.json`, `characters.json`, chapter folders, moods, segments, and filters.

Poetry pipelines use `model.json` and `bookseed.txt` as source of truth, one segment per topic, and no `mood.json` unless explicitly configured as a hybrid.

### Segment Drafts

Intermediate segment work stays inside `.space/pipeline/`:

```text
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/writer/
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/editor/
.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/translator/
```

Do not write unfinished drafts directly to `source/books/`.

### Filter Outputs

Filters write only inside the pipeline filter folders resolved by:

```text
.space/pipeline/book_<bookname>/filters/filters.json
```

If a registry exists, use it to resolve:

```text
folder
role_file
summary_file
output_file
```

If no registry exists, follow `.framework/workflows/write.md` and the current pipeline layout.

### Final Output

Verified, finalized text is promoted to:

```text
source/books/book_<bookname>/chapters/
source/books/book_<bookname>/book.md
```

Only promote text after the required validation filters have passed.

## Validation And Promotion Rules

Before writing to `source/books/`, apply the pipeline filters in the order specified by `.framework/workflows/write.md`.

For novels, the full validation chain is:

```text
workshop -> research -> seeds -> correctness -> theme -> syntax -> override -> quality
```

For poetry, the full validation chain is:

```text
research -> correctness -> theme -> syntax -> override -> quality
```

`quality` is the final gate. Do not mark a chapter complete or promote it to final output until quality has passed or the workflow explicitly records an accepted human override.

## Safety And Structure Constraints

- Never alter the repository directory structure unless the active workflow explicitly requires it.
- Never create root-level chapter folders under `.space/pipeline/book_<bookname>/`.
- Never create segment folders outside `chapters/<chapter>/segments/<segment>/`.
- Never move, rename, delete, or overwrite user-authored content without first reading it and confirming the workflow requires the change.
- Never re-scaffold an existing pipeline from scratch unless the user explicitly asks.
- Preserve existing pipeline state and resume from it.
- Maintain the configured authorial tone, signature, language, register, syntax sample, reference, and theme set.
- Prefer existing framework agents, skills, templates, and rules over new abstractions.
- Keep runtime outputs in `.space/pipeline/` until validation permits promotion.
- Keep finished, reader-facing text in `source/books/` only.

## Operating Procedure

For every `/write` request:

1. Read this `AGENTS.md` file.
2. Read `.framework/workflows/write.md`.
3. Parse the target book, unit/chapter/segment, signature/persona, and stage/role from the user arguments.
4. Inspect the relevant `.space/backlog/`, `.space/pipeline/`, and `source/books/` paths before writing.
5. Select the responsible agent from `.framework/agents/`.
6. Let that agent invoke any required skill.
7. Write intermediate outputs only to the pipeline.
8. Run the required filters and validations.
9. Promote final text to `source/books/` only after validation passes.
10. Report what changed, what was validated, and what remains pending.


