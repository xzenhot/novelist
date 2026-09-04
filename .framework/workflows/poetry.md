---
name: writer
description: Alias for the unified writer workflow. The poetry form is a verse book (config-driven, Question/Oration/Benediction chapters, 6 filters). See .framework/workflows/write.md for the full engine.
tools: ["read", "write"]
---

# The Prophet Agent (alias)

This file is a **thin alias** for the unified writer workflow at `.framework/workflows/write.md`.

The poetry form is defined by `"form": "poetry"` in the pipeline's `config.json`. Read `.framework/workflows/write.md` for the complete engine — command system, scaffolding, the filter command, stereotype selection, and writing rules. The poetry-specific behavior is:

- **Source of truth:** `.space/pipeline/book_<bookname>/config.json` + `bookseed.txt`
- **Chapter structure:** Question / Oration / Benediction
- **Segments per chapter:** exactly one
- **Filter chain (6):** research → correctness → theme → syntax → override → quality
- **Word target:** 500–800 words
- **Stereotype templates:** `.framework/templates/stereotypes/poetry/`

The command is `/write <bookname> ...`.
