# Novel Scaffolding Logic - v1

This file is intentionally downgraded to a short reference note.

The authoritative scaffolding instructions now live in:

`../../../.framework/skills/layout/SKILL.md`

Use that layout skill when creating or repairing a novel pipeline.

## Canonical Template

Use the v1 fiction book template:

` .space/templates/v1/fiction/book/ `

A scaffolded book pipeline must live under:

` .space/pipeline/book_<bookname>/ `

Finished output must live under:

` source/books/book_<bookname>/ `

## Mandatory Path Invariant

- The only valid chapter path is `book_<bookname>/chapters/chapter_<n>/`.
- The only valid segment path is `book_<bookname>/chapters/chapter_<n>/segments/segment_<x>/`.
- Never create `chapter_<n>/`, `chapter<n>/`, or `chapterN/` directly under `book_<bookname>/`.
- Never create `segment_<x>/`, `segment<x>/`, or `segmentN/` outside `chapters/chapter_<n>/segments/`.

## Minimal Scaffold Summary

1. Copy book-level `Template*` files from `.space/templates/v1/fiction/book/` into `.space/pipeline/book_<bookname>/`.
2. Copy `.space/templates/v1/fiction/book/chapters/chapter_1/` into `.space/pipeline/book_<bookname>/chapters/chapter_1/`.
3. Preserve the nested segment path: `chapters/chapter_1/segments/segment_1/`.
4. Seed the book-level layout/model/meta JSON files from the user gist.
5. Create `source/books/book_<bookname>/`.
6. Verify the path invariant.

## OperationState Reference

For the full file-name/state mapping, see:

`FileName.md`
