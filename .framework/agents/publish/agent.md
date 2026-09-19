---
name: publish
description: Publishes chapter-root chapter.md files with titles from the matching chapter model.json into a new source/books version and assembles book.md. Read-only on the pipeline except progress.json; never selects writer, translator, or archived segment files.
tools: ["read", "write"]
---

# The Publish Agent

Publish the current chapter-root drafts as a versioned, reader-facing book. Use the same source selection, title handling, ordering, and progress semantics as `.tools/publish.py`.

## Inputs

1. Command: `/book <bookname> publish`. The corresponding helper is `python .tools/publish.py <bookname>`.
2. `.space/pipeline/<bookname>/chapters/` must exist; otherwise stop and require scaffold.
3. `.space/pipeline/<bookname>/model.json` supplies the book title through `book_long_title`, falling back to the book name when empty or absent.
4. Each chapter's only content source is `.space/pipeline/<bookname>/chapters/<n>/chapter.md`.
5. Each chapter's title comes exclusively from `chapter_title` in `.space/pipeline/<bookname>/chapters/<n>/model.json`.
6. Read `progress.json` if it exists, preserving unrelated fields for the final progress update.

Language-based source selection is no longer supported. Do not interpret a language argument as permission to publish translator files; report the supported command instead. This source-selection contract supersedes older writer/translator selection instructions in the workflow.

## Chapter Selection and Validation

1. Inspect immediate chapter directories only. Include numeric names and the named units `Introduction` and `Conclusion`; ignore unrelated directories.
2. Order chapters as `Introduction`, numeric chapters in ascending numeric order, then `Conclusion`. Use actual folders rather than deriving chapter numbers from the length of `bookseed.txt`.
3. Read each chapter-root `chapter.md` and matching `model.json` as UTF-8, accepting a BOM. Require readable, valid chapter metadata with a nonempty string `chapter_title` and nonempty draft text.
4. Skip and report each chapter with missing/unreadable files, invalid metadata, a missing/blank title, or an empty draft. Never fall back to the summary, topic list, writer folder, translator folder, or any version archive.
5. Normalize whitespace in the title to a single line. Trim surrounding draft whitespace. If the draft starts with a Markdown heading (`#` through `######` followed by whitespace), remove that first line so the model title replaces the previous heading. Preserve the remaining body and its internal headings. Skip a draft that contains only a heading.
6. Collect usable chapters before allocating an output version. If none remain, report that nothing can be published; create no output version and do not update progress.
7. Retain the repository's required quality/promotion gate. Source selection does not itself establish that a chapter has passed validation; do not invent a pass or mark unfinished work complete.

## Version Allocation

1. Inspect `source/books/<bookname>/` for directories named exactly `version<k>`, with a numeric suffix.
2. Allocate the next integer above the highest existing version, starting with `version1`.
3. Create the version directory exclusively. If another publisher claims it, try the next number. Never reuse or overwrite an existing version.
4. All output of this invocation belongs under that newly allocated directory.

## Chapter Output

For each usable chapter, write:

```text
source/books/<bookname>/version<k>/chapters/<n>/chapter.md
```

The output contains `# <chapter_title>`, a blank line, and the preserved body. Title replacement is formatting, not permission to rewrite the body. Do not copy segment metadata or create language subfolders.

## Book Assembly

Write `source/books/<bookname>/version<k>/book.md` with:

- `# <book_long_title>` (or the book name fallback).
- Each published chapter in the selection order, introduced by `## <chapter_title>` from its chapter model.
- A `---` separator between chapters.

Use the same body text as the per-chapter output, without duplicating its level-one title. Do not create `book_<language>.md` or infer titles from draft text.

## Progress Update

If `progress.json` exists, merge these fields after output is successfully written:

- `published`: `true` only when no selected chapters were skipped; otherwise `false`.
- `published_at`: the UTC publication timestamp.
- `published_version`: the newly allocated numeric version.
- `published_chapters`: the chapter folder names successfully published in this invocation.
- `skipped_chapters`: the chapter folder names skipped in this invocation.

Remove a stale `published_language` field because this command has no language-specific mode. Preserve all other filter, completion, and writing state. If progress.json does not exist, do not create it; report that no progress file was available.

## Rules

- The only pipeline file this agent may modify is an existing `progress.json`.
- Never read chapter content from `segments/<x>/writer/`, `segments/<x>/translator/`, `segments/<x>/version/`, or `history/`.
- Never modify the chapter-root draft or chapter model while publishing.
- Never run filters, styles, translations, or chapter-writing agents during publication.
- Preserve previous published versions and report all skipped chapters with reasons.

## Output Contract

Report the new version number and folder, published/skipped counts and skip reasons, the assembled `book.md` path, and whether progress.json was updated or absent. If no chapter was publishable, report that no version was created.
