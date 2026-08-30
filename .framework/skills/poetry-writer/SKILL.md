---
name: poetry-writer
description: 'Write, scaffold, revise, and audit Gibran-esque philosophical poetic prose books. Use when the user asks to write poetry, write a book of poetic prose, scaffold a new poetry book, continue/resume a book, revise or tighten a chapter, audit completed chapters, or list available qualities/themes/references. Transforms a list of topics/terms into prophetic chapters grounded in a reference book (e.g. Marcus Aurelius, Lalon Shah).'
argument-hint: '<bookname> [quality] [theme] [reference] | [count|chapter|range] | -o | -h'
---

# Poetry Writer — The Prophet Agent

A dynamic, subject-agnostic literary engine that expands a list of topics/terms into full-length philosophical poetic prose chapters in the voice of Kahlil Gibran's *The Prophet* (1923). The writing *style* is fixed; the *subject, language, and philosophical grounding* are parameterized per book.

## When to Use

- "write poetry", "write a book", "write chapters", "scaffold a new book", "create a book"
- "continue writing", "resume", "write 5 more", "write chapter 34", "write chapters 20–25"
- "revise chapter 7", "tighten chapter 3", "make chapter 5 more archaic", "audit completed chapters"
- "list options", "what qualities/themes/references are available"

## Architecture

The engine is split into two layers, both already present in this repo:

| File | Role |
|------|------|
| `.framework/workflows/poetry.md` | **The writing engine.** Voice, structural formula, style rules, execution steps, and the full command spec. Subject-agnostic — never changes between books. |
| `.framework/workflows/reframe.md` | **The reframer engine.** Reshapes already-written chapters (voice, register, dialect, structure) while preserving their philosophical core. |
| `.framework/workflows/guide.md` | Human-facing implementation guide (architecture, inputs, output files, workflow). |
| `.space/context/` | Shared inputs: `qualities/` (seed analyses), `themes/` (thematic categories), `references/` (source texts), each with a `registry.md`. |
| `.space/templates/poetry/default/` | The canonical book template (`config.json`, `bookseed.txt`, `override.md`, `progress.json`, `chapters/`). |
| `.space/pipeline/book_<name>/` | Per-book **inputs** (config, index, override, metadata, progress). |
| `source/book_<name>/` | Per-book **outputs** (finished chapters, `book.md`). |

**Read `.framework/workflows/poetry.md` first** — it is the authoritative engine and command spec. This skill is the entry point and workflow map; the engine holds the full procedural detail.

## The Three Pillars (woven into every chapter)

1. **Context** (dynamic) — the reference book and its analysis: quality metrics, core themes, metaphor families, thematic categories.
2. **Style** (fixed) — the Gibran-esque voice: biblical cadence, sacred vocabulary, and the Question → Oration → Benediction structure.
3. **Theme** (dynamic) — the thematic category assigned to each chapter, cycled in order.

## Commands

```
/write <bookname> <quality> <theme> <reference>   # scaffold a new book
/write <bookname> [<book_seed>]                  # write chapters (uses bookseed.txt)
/write -h | --help                               # show usage
/write -o | --options                            # list qualities, themes, references
```

- **scaffold** — create `.space/pipeline/book_<name>/` (config, blank `bookseed.txt`, `override.md`, `metadata_code1.json`) and `source/book_<name>/chapters/`.
- **write** — generate chapters from `bookseed.txt`; supports counts, "5 more", a specific number, or a range.
- **revise / audit** — transform or inspect existing chapters (see `.framework/workflows/reframe.md` and the revision rules in `.framework/workflows/poetry.md`).
- **options** — read the three `registry.md` files and print their catalogs.

## Procedure (write mode)

1. **Read config** — `.space/pipeline/book_<name>/config.json` → title, `language` (authoritative for output language), register, and paths to quality/themes/reference/index.
2. **Read context** — the quality file, themes file, and reference book (if provided).
3. **Read index** — `bookseed.txt` (one subject per line; each becomes one chapter).
4. **Read override** (optional) — `override.md`; if filled, apply its four transformation passes in order.
5. **Reconcile progress** — compare `bookseed.txt` against `progress.json`; add/remove/renumber, preserve `completed`, update `total_chapters`.
6. **Select next chapter** — first `pending`/`in_progress`; assign the next thematic category (cycling).
7. **Generate** — 500–800 words in the config's language, Question → Oration → Benediction, term translated to soul-language.
8. **Apply override** — Prompt Transformation → Local Preferences → Local Dialects → Slug/Location/Era.
9. **Save** — `source/book_<name>/chapters/Chapter_XXX_[term].md`, heading `# অধ্যায় XXX: [term]` (or target-language equivalent).
10. **Append** — add to `source/book_<name>/book.md` after a `---` separator.
11. **Update progress** — mark completed, timestamp, bump counters.
12. **Report** — chapter number, progress, offer to continue.

## Key Rules

- **`config.json` is the single source of truth** for how to write; `bookseed.txt` for *what* to write; `progress.json` for *how far along*.
- **`language` in `config.json` is authoritative** — change it and the next run writes in the new language.
- **`bookseed.txt` and `override.md` are the only human-editable files.** Never hand-edit `config.json`, `progress.json`, `chapters/`, or `book.md`.
- **Metadata files are append-only** — each run creates the next `metadata_code<number>.json`; never overwrite.
- **Resume, never restart** — always read `progress.json` first; never restart from Chapter 1 unless asked.
- **Write to disk, never only to chat** — every chapter produces a chapter file and a `book.md` append.

## References

- Engine & command spec: [`.framework/workflows/poetry.md`](../../../.framework/workflows/poetry.md)
- Reframer engine: [`.framework/workflows/reframe.md`](../../../.framework/workflows/reframe.md)
- Implementation guide: [`.framework/workflows/guide.md`](../../../.framework/workflows/guide.md)
- Book template: [`.space/templates/poetry/default/`](../../../.space/templates/poetry/default/)
- Context registries: [`.space/context/qualities/registry.md`](../../../.space/context/qualities/registry.md), [`.space/context/themes/registry.md`](../../../.space/context/themes/registry.md), [`.space/context/references/registry.md`](../../../.space/context/references/registry.md)
