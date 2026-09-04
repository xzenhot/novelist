---
name: novel-writer
description: Alias for the unified writer workflow. The novel form is a prose book (epic-driven, Workshop/Story/Discussion chapters, 8 filters). See .framework/workflows/write.md for the full engine.
tools: ["read", "write"]
---

# Novel Writing Agent (alias)

This file is a **thin alias** for the unified writer workflow at `.framework/workflows/write.md`.

The novel form is defined by `"form": "novel"` in the pipeline's `book.json`. Read `.framework/workflows/write.md` for the complete engine — command system, scaffolding, the filter command, stereotype selection, and writing rules. The novel-specific behavior is:

- **Source of truth:** `.space/backlog/epic/<bookname>/epic.md`
- **Chapter structure:** Workshop / Story / Discussion
- **Segments per chapter:** many
- **Filter chain (8):** workshop → research → seeds → correctness → theme → syntax → override → quality
- **Word target:** 5,500+ words
- **Stereotype templates:** `.framework/templates/stereotypes/novel/`

The command is `/write <bookname> ...` (the `/novel` command name is retained as a synonym for backward compatibility).
