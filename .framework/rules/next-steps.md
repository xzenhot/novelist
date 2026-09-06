# Next Steps Rule

Every time a `/write` command completes, the runtime must report what changed and then display the most logical next steps for the user. This rule applies to all `/write` subcommands and all forms (novel, poetry).

## What to Show

After finishing the requested work, append a concise **Next Steps** section to the response that contains:

1. **What just happened** — one or two lines summarizing the state change (e.g., "Created backlog epic", "Scaffolded pipeline", "Wrote chapter 3", "Ran syntax filter").
2. **The natural next action** — the single most useful command to run next, based on the command that just completed.
3. **Optional follow-ups** — up to two additional commands that make sense at this point, ordered by usefulness.

## Next-Step Mapping by Command

Use this table to choose the recommended follow-up command. Remember the boundary: backlog commands (1–3) never touch the pipeline, and pipeline commands (4–10) never touch the backlog.

| Completed command | State after completion | Recommended next step | Optional follow-ups |
|---|---|---|---|
| `/write <bookname>` (bare) | Backlog epic exists; no pipeline | `/write <bookname> init [preset]` | `/write <bookname> scaffold <gist> count <n>` (after init) |
| `/write <bookname> gist [<gist>]` | Backlog epic created, updated, or rewritten; no pipeline | `/write <bookname> init [preset]` | `/write <bookname> scaffold <gist> count <n>` (after init) |
| `/write <bookname> init [<preset>]` | Preset selected; filter chain configured; pipeline may or may not exist | If pipeline exists: `/write <bookname> filter all`<br>If pipeline missing: `/write <bookname> scaffold <gist> count <n>` | `/write <bookname> chapter all` (if pipeline exists and chapters are ready) |
| `/write <bookname> scaffold <gist> count <n>` | Pipeline and chapter structure exist; research not yet run | `/write <bookname> filter all` | `/write <bookname> chapter all` |
| `/write <bookname> chapter <target>` | One or more chapters written to `source/books/` or pending | If chapters remain: `/write <bookname> chapter continue`<br>If all chapters complete: `/write <bookname> filter quality` or final assembly | `/write <bookname> filter <next-filter>` |
| `/write <bookname> chapter all` | All canonical chapters attempted | `/write <bookname> filter all` | `/write <bookname> filter quality` |
| `/write <bookname> chapter continue` | Resumed and wrote remaining chapters, or none were pending | If chapters remain pending: `/write <bookname> chapter continue`<br>If complete: `/write <bookname> filter quality` | `/write <bookname> filter all` |
| `/write <bookname> filter <filter>` | Single filter completed | Next filter in chain: `/write <bookname> filter <next>` | `/write <bookname> filter all` |
| `/write <bookname> filter all` | Full filter chain completed | `/write <bookname> chapter all` or `/write <bookname> chapter continue` | `/write <bookname> filter quality` |
| `/write <bookname> filter quality` | Quality gate passed or recorded | `/write <bookname> chapter all` or final promotion to `source/books/book_<bookname>/book.md` | Review `source/books/book_<bookname>/chapters/` |
| `/write <bookname> add <n> filter <filter>` | New chapters added; filter run on new chapters | `/write <bookname> chapter continue` | `/write <bookname> filter all` |
| `/write <bookname> form <formname>` | Form changed in `model.json` | `/write <bookname> scaffold` (if structure needs rebuilding) | `/write <bookname> config show` |
| `/write <bookname> config [<key> [<value>]]` | Configuration inspected or updated | `/write <bookname> chapter all` | `/write <bookname> filter all` |
| `/write -o` / `--options` | Read-only list displayed | Choose any book and run its next logical command | `/write <bookname> chapter continue` |
| `/write -h` / `--help` | Help displayed | Choose a `/write` command to run | — |

## Determining the Next Filter

When recommending a single next filter, look up the current filter chain in `.space/pipeline/book_<bookname>/filters/filters.json` and suggest the filter with the next higher `order` value after the one just completed. If the completed filter was the last in the chain, recommend the `chapter all` command instead.

## Format

Present the section as plain Markdown:

```markdown
Next steps:
- Recommended: `/write <bookname> <command>` — short reason
- Optional: `/write <bookname> <command>` — short reason
- Optional: `/write <bookname> <command>` — short reason
```

Keep each reason to one line. Do not invent commands that do not exist in `.framework/workflows/write.md`.
