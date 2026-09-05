# Workshop Filter Role

## Purpose

Create the three-section chapter frame for each novel chapter: **Workshop**, **Story**, and **Discussion**. The frame is grounded in the epic and the chapter plan, and it provides the structure the later writer agent will fill.

## Inputs

- `.space/backlog/epic/<bookname>/epic.md`
- `.space/pipeline/book_<bookname>/book.json` chapter summaries
- `.space/pipeline/book_<bookname>/characters.json`
- `.space/pipeline/book_<bookname>/workshop_metadata.md`

## Outputs

For each chapter, write a file at `.space/pipeline/book_<bookname>/filters/workshop/<chapter>.md` containing:

1. **Workshop** — a short modern-frame scene (scribe, guard, hill) that introduces the chapter's memory.
2. **Story** — a placeholder summary of the historical narrative to be written, drawn from the epic and chapter plan.
3. **Discussion** — a short response from the frame characters after the story is told, linking to the next chapter.

## Rules

- The Introduction's Workshop must hint at the larger story's consequence and carry suspense.
- Keep Workshop and Discussion short but resonant; the Story placeholder should indicate the chapter's dramatic center.
- Do not write full chapter prose here; only frame and summarize.
