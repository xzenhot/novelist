---
name: workshop-director
description: 'Conduct workshops for a novel layout. Use when the user asks to run a workshop, conduct a workshop, write workshop minutes, generate a workshop scene, or produce the workshop narrative for a chapter. Turns a novel layout (book.json + characters.json + workshop_metadata.md) into workshop_minutes/<chapter>.md files with the three-section frame-story structure.'
argument-hint: '<bookname> <chapter> | all | continue | -o | -h'
---

# Workshop Director — Frame-Story Workshop Engine

Conducts the **workshop** that frames each chapter of a frame-story novel. Every chapter is born in a workshop: the modern theatre troupe gathers, discusses, and the narrator (বিশ্বরূপ বিশ্বাস) reads the historical narrative aloud. The workshop minutes are the raw material the writing engine later turns into finished chapters.

## When to Use

- "run a workshop", "conduct a workshop", "write workshop minutes", "generate a workshop"
- "workshop for chapter 3", "workshop all chapters", "continue the workshops"
- "who attends the workshop", "list workshops"

## The Workshop Structure

Each workshop produces one file: `.space/pipeline/book_<bookname>/workshop_minutes/<chapter>.md`, where `<chapter>` is `Introduction`, `1..N`, or `Conclusion`.

Every workshop file has **three sections**:

| Section | Bengali | Role |
|---------|---------|------|
| **বিভাগ ১ — ওয়ার্কশপ** | The Workshop | The modern frame: the troupe gathers, discusses, and the director prompts the narrator. |
| **বিভাগ ২ — গল্প** | The Story | The historical narrative, read aloud by the narrator (বিশ্বরূপ বিশ্বাস). |
| **বিভাগ ৩ — আলোচনা** | The Discussion | The troupe's reaction after the reading — laughter, debate, or serious analysis. |

## Inputs (read before conducting)

| File | What it provides |
|------|------------------|
| `.space/pipeline/book_<bookname>/book.json` | The chapter list — each chapter's `chapter_title` and `chapter_summary`. |
| `.space/pipeline/book_<bookname>/characters.json` | The cast — real and fictional characters. |
| `.space/pipeline/book_<bookname>/workshop_metadata.md` | The troupe roster (core members, advisors, diverse participants) and attendance rules. |
| `.space/pipeline/book_<bookname>/masterprompt.md` | The book-specific persona and chapter guidelines. |

## Commands

```
/workshop <bookname> <chapter>   # conduct one workshop (Introduction, 1..N, Conclusion)
/workshop <bookname> all         # conduct all workshops in order
/workshop <bookname> continue    # resume from the first missing workshop
/workshop <bookname> -o          # list existing workshops
/workshop -h | --help            # show usage
```

## Procedure

1. **Read the layout** — `book.json` for the chapter's title/summary, `characters.json` for the cast, `workshop_metadata.md` for the troupe and attendance rules, `masterprompt.md` for the persona.
2. **Pick attendance** — follow the attendance rules in `workshop_metadata.md`:
   - Core members: 5–6 (the director মোহিত কাঞ্জিলাল and narrator বিশ্বরূপ বিশ্বাস are **always present**).
   - Advisors/guest artists: 1–2.
   - Diverse participants: 1–2.
   - Name the present members explicitly; briefly hint why the absent ones are away.
3. **Write বিভাগ ১ (Workshop)** — the modern frame. The troupe discusses the upcoming chapter; their questions, curiosity, or debate become the **trigger** that leads the narrator to begin reading.
4. **Write বিভাগ ২ (Story)** — the historical narrative, grounded in the chapter's `chapter_summary` and the cast from `characters.json`. This is the actual story.
5. **Write বিভাগ ৩ (Discussion)** — the troupe's reaction after the reading, plus a **running summary** that sets up the next chapter.
6. **Save** — write to `.space/pipeline/book_<bookname>/workshop_minutes/<chapter>.md`.
7. **Report** — which workshop was conducted and what the next one will cover.

## Key Rules

- **The workshop is the frame, not the finished chapter.** The writing engine (`novelist` skill / `novel.md`) later rewrites বিভাগ ২ into polished prose; the workshop minutes are the raw narrative.
- **The narrator is always বিশ্বরূপ বিশ্বাস** — he reads বিভাগ ২ aloud; the director মোহিত কাঞ্জিলাল always conducts.
- **Attendance is random but bounded** — follow the ratios in `workshop_metadata.md`; never have everyone present.
- **Each workshop ends with a running summary** — a bridge to the next chapter that keeps the reader's curiosity alive.
- **`Introduction` is always first, `Conclusion` last** — the N main chapters sit between them.
- **Resume, never restart** — `continue` starts from the first missing workshop file.

## References

- Canonical example: [`.space/pipeline/book_laxman/workshop_minutes/`](../../../.space/pipeline/book_laxman/workshop_minutes/)
- Workshop metadata (troupe roster): [`.space/pipeline/book_laxman/workshop_metadata.md`](../../../.space/pipeline/book_laxman/workshop_metadata.md)
- Novel layout & engine: [`novelist` skill](../novelist/SKILL.md) and [`.framework/workflows/novel.md`](../../../.framework/workflows/novel.md)
