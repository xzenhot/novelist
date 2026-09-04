# Implementation Guide for the Writer Agent

This guide explains how to set up and run the **writer agent** — a subject-agnostic literary engine that transforms workshop narratives (novel) or topic lists (poetry) into full-length chapters. It weaves three things at runtime — **Context** (the reference/grounding), **Style** (the selected voice), and **Theme** (the thematic categories) — into every chapter.

The engine is defined in a single file, `.framework/workflows/write.md`, and branches on a **`form`** discriminator (`novel` or `poetry`).

> **Shared rule:** the filter concept is defined in `.framework/rules/filters.md` and applies to all workflows. Every book pipeline passes its material through a set of filters, each owning a folder in the pipeline.

---

## Architecture Overview

| File | Role |
|------|------|
| `.framework/workflows/write.md` | **The writing engine.** Defines the command system, scaffolding, filter command, stereotype selection, and writing rules. Subject-agnostic — never changes between books. |
| `.space/pipeline/book_<bookname>/` | **The book pipeline.** Holds the book's inputs (epic or config, characters, filters, chapters). |
| `.space/backlog/epic/<bookname>/epic.md` | **The epic (novel only).** The single source of truth for a novel's story. |
| `.space/pipeline/book_<bookname>/config.json` | **The config (poetry only).** The source of truth for a poetry book — language, register, quality, themes, reference, index. |
| `.space/pipeline/book_<bookname>/bookseed.txt` | **The index (poetry only).** The list of topics/terms, one per line. Each becomes one chapter. |
| `.framework/templates/stereotypes/<form>/` | **The stereotype templates.** Signatures, references, themes, and syntax samples for each form. |
| `source/books/book_<bookname>/` | **The finished book.** Chapters in `chapters/`, consolidated `book.md` at the root. |

To write a *new* book, you scaffold a new pipeline under `.space/pipeline/` and write to `source/books/`. The engine in `write.md` stays untouched.

---

## The Form Discriminator

A book is either a **novel** (prose) or **poetry** (verse). The form is declared once, at scaffold time, in the pipeline's `form` field, and read everywhere else.

```json
// book.json (novel)  OR  config.json (poetry)
"form": "novel"   // or "poetry"
```

| Signal | Novel | Poetry |
|---|---|---|
| **`form` field** | `"novel"` | `"poetry"` |
| **Source of truth** | `epic.md` (epic-driven) | `config.json` + `bookseed.txt` |
| **Chapter structure** | Workshop / Story / Discussion | Question / Oration / Benediction |
| **Segments per chapter** | many | exactly one |
| **`mood.json`** | present per chapter | absent |
| **Filter chain** | 8 filters | 6 filters |
| **Word target** | 5,500+ words | 500–800 words |
| **Stereotype templates** | `stereotypes/novel/` | `stereotypes/poetry/` |

---

## The Command System

```text
Usage: /write <bookname> [<gist>] [--form novel|poetry]   # scaffold a new book pipeline
       /write <bookname> chapter <chapter>|<n>|all|continue  # write a chapter (or all/remaining)
       /write <bookname> filter <filter>|*|all            # run a filter (or all)
       /write <bookname> form <formname>                  # set/change the book's form
       /write <bookname> config [<key> [<value>]]         # get or set the book's model config
       /write <bookname> config show                      # show the book's model config
       /write -h | --help                                 # show this help
       /write -o | --options                              # list available books and chapters
```

| Command | What it does |
|---------|--------------|
| `scaffold` | Create or repair the pipeline from the layout skill. |
| `chapter <chapter>\|<n>\|all\|continue` | Write one chapter, a numbered chapter, all chapters, or the remaining chapters. |
| `filter <filter>\|*\|all` | Run a single filter, or all filters in order. |
| `form <formname>` | Set or change the book's form (`novel` / `poetry`). |
| `config [<key> [<value>]]` | Get or set the book's model config (signature, reference, theme set, syntax). |
| `config show` | Show the book's model config. |
| `options` | List available books and chapters. |
| `help` | Show usage. |

---

## The Filter Chains

The filter chain depends on the form.

**Novel (8 filters):**

```
workshop → research → seeds → correctness → theme → syntax → override → quality
```

**Poetry (6 filters):**

```
research → correctness → theme → syntax → override → quality
```

Each filter is backed by a role agent (novel) or a skill (poetry), and owns a folder in `.space/pipeline/book_<bookname>/filters/`. The `override` and `quality` filters are human-in-the-loop: they generate a context-aware `filter.md` (novel) or read `override.md` (poetry) and apply any human instructions written there.

---

## The Stereotype Selection

Every chapter is rendered in a **form** — novel (prose) or poetry (verse). Based on that form, the theme and syntax filters select from the stereotype templates:

- **Signature** — the voice that renders the chapter: `stereotypes/<form>/signatures/`
- **Reference** — the source text for grounding: `stereotypes/<form>/references/`
- **Theme set** — the philosophical lens: `stereotypes/<form>/themes/`
- **Syntax sample** — the target sentence structure: `stereotypes/<form>/syntax/`

Read the `registry.md` in each folder to discover available options, then read the chosen file for the full definition. The selections must be mutually consistent — same form, and where possible the same author or tradition.

---

## Output Layout

Finished chapters live in a `chapters/` subfolder, and the consolidated book lives at the book root.

```
source/books/book_<bookname>/
├── book.md              ← the consolidated book (at root)
└── chapters/
    ├── Introduction.md
    ├── 1.md … N.md
    └── Conclusion.md
```

After all chapters are written, assemble `book.md` at the book root: open with the title and gist epigraph, append every chapter in order, separate with `---` dividers, and ensure both an Introduction and a Conclusion exist.

---

## Recommended Workflow

1. **Scaffold** — `/write <bookname> <gist>` creates the pipeline and the epic (novel) or config (poetry).
2. **Run the filters** — `/write <bookname> filter *` runs the full filter chain.
3. **Write the chapters** — `/write <bookname> chapter all` writes every chapter.
4. **Assemble the book** — the `chapter all` command assembles `book.md` at the book root.
5. **Refine** — use `config` to change the signature/theme, or `override`/`quality` for human-in-the-loop edits.

---

## Progress Tracking

The agent always checks the pipeline's state before writing, so it can **resume** from where it left off — never restarting from the beginning unless explicitly asked. The `chapter continue` command resumes from the first missing chapter.
