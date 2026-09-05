# Workshop Filter

## Purpose

Produce the per-chapter workshop narrative: the modern frame scene (Workshop / Story / Discussion) that becomes the chapter's first-pass content.

## Inputs

- `.space/backlog/epic/<bookname>/epic.md` — the epic source of truth.
- `.space/pipeline/book_<bookname>/book.json` — book structure and chapter summaries.
- `.space/pipeline/book_<bookname>/masterprompt.md` — voice, frame, and style mandate.

## Outputs

- `filters/1/Introduction.md`
- `filters/1/1.md` … `filters/1/N.md`
- `filters/1/Conclusion.md`

Each file contains three sections: **Workshop**, **Story**, **Discussion**.

## Rules

1. The Workshop section is a modern frame scene where narrators discuss the chapter's subject.
2. The Story section narrates the chapter's historical or emotional events in brief.
3. The Discussion section closes the frame with a reflective exchange.
4. The Introduction must hint at the larger epic arc and carry suspense.

## Hand-off

The next filter (`2`) reads the Story section to ground research for each chapter.
