# Agentic Harness Review — TODO

## Tier 1 — Critical Inconsistencies (likely to cause runtime failures)

**1. Filter chain mismatch between novel and poetry**
The `guide.md`, `workflows/book.md`, and `rules/filters.md` each define the filter chains differently. For example:
- `guide.md` says the novel chain is `workshop → research → seeds → correctness → theme → syntax` (no `override`, no `quality`)
- `rules/filters.md` shows the full 8-step default including `override` and `quality`
- `AGENTS.md` says the novel chain ends at `syntax`, but poetry includes `override → quality`
- The `quality` agent still hardcodes path `filters/8/filter.md` instead of `filters/quality/filter.md` — a direct file path bug

**2. `reframe` agent is a legacy island**
The `reframe` agent (`agent.md` name is `reframer`) reads from `source/<bookname>/config.json` and `source/<bookname>/chapters/` — a completely different path convention than the rest of the pipeline. It doesn't use `.space/pipeline/` at all. It would fail silently or corrupt the pipeline layout.

**3. `seeds` agent is a novel-only agent in a form-aware pipeline**
The seeds agent reads `mood.json`, `characters.json`, and segment structure in a way that only applies to novels. For poetry (no moods, one segment per chapter), it would create incorrect structure. The `workshop` agent has a form-dispatch (poetry/novel) but `seeds` does not.

**4. Segment count contract conflict**
`scaffold/agent.md` says poetry has exactly one segment per chapter. `seeds/agent.md` says it determines segment count from chapter length and "epic material" — meaning it could create multiple segments for poetry chapters, violating the invariant.

---

## Tier 2 — Design Gaps (will limit reliability or extensibility)

**5. No error recovery / idempotency contract**
Agents don't define what happens when they're re-run on a chapter that's already been processed. The `write` agent increments version numbers, but filter agents overwrite `chapter.md` without a clear re-run policy. The `enrich` agent in particular fuses all active filters but doesn't snapshot what it consumed.

**6. `progress.json` schema is undefined**
Multiple agents reference `progress.json` but none define its schema. The `publish` agent writes to it, `chapter` agent reads it, and the `write` workflow uses it for `continue`. There's no canonical schema document.

**7. `enrich` always disables `workshop` and `override`**
The `enrich` agent hardcodes `workshop` and `override` as non-autorun. This is a design decision buried inside an agent rather than declared in `filters.json`. If someone sets `override.autorun = true` in the registry, `enrich` would silently ignore it.

**8. Language handling is inconsistently sourced**
Some agents read language from `book.json`, others from `model.json`, others from `config.json` (reframe). There's no single authoritative resolution order across all agents.

**9. Version allocation is uncoordinated**
The `chapter` agent notes it should stop if the destination path "already exists" (to avoid collision), but `publish` agent allocates `version<k+1>` independently. Two concurrent write passes could allocate the same version.

**10. MCP research tool path is hardcoded to a specific repository**
`research/agent.md` hardcodes the repo root as `d:\lab\github\Gibran\novelist` — a specific, different project. This would fail in the current `writer` repo.

---

## Tier 3 — Clarity and Maintainability Issues

**11. `command-boundary.md` is stale**
The command boundary rule (`.framework/rules/command-boundary.md`) still references the `gist` subcommand as command #2 — but `guide.md` and `workflow/book.md` say the `gist` subcommand was merged into the bare bookname command. The rule is out of sync.

**12. `AGENTS.md` and `book.md` have overlapping but divergent command references**
Both define the full command surface. `AGENTS.md` is the runtime steering doc; `book.md` is the workflow spec. They should be the single source of truth but they partially duplicate and partially contradict (e.g., `AGENTS.md` lists `prelayout/postlayout` as agents but doesn't define how they're invoked; `book.md` does it inline).

**13. Agent front-matter `tools` field is inconsistent**
Some agents declare `tools: ["read", "write", "mcp"]` (research), some `tools: ["read", "write"]`. No agent defines what "mcp" actually enables. The `mcp` tool dependency in `research` is the only external runtime dependency in the system and it's not documented at the harness level.

**14. `reframe` agent identity is `reframer` but folder is `reframe`**
The front-matter `name: reframer` doesn't match the folder name `agents/reframe/`. Agent resolution by name would fail.

---

## Proposed Execution Plan

### Phase A — Audit (read all files, no writes)
Read every agent, skill, rule, and template. Build a complete cross-reference: what each agent reads, writes, and depends on. Surface all inconsistencies.

### Phase B — Fix critical bugs
- Fix the `quality` agent filter path (`filters/8/` → `filters/quality/`)
- Fix the `reframe` agent front-matter name and path conventions
- Define and document `progress.json` schema
- Add form-dispatch to `seeds` agent (or restrict it to novel-only and add a poetry equivalent)

### Phase C — Harmonize the filter chain
Produce a single canonical filter chain definition for each form. Update `AGENTS.md`, `guide.md`, `workflows/book.md`, and `rules/filters.md` to all reference the same source of truth.

### Phase D — Strengthen agent contracts
Add idempotency rules (what re-running a filter on an already-processed chapter should do). Define language resolution order. Standardize `progress.json` updates.

### Phase E — Refactor legacy artifacts
Migrate `reframe` agent to use `.space/pipeline/` conventions or formally document it as a standalone tool. Remove the hardcoded repo path from `research` agent.
