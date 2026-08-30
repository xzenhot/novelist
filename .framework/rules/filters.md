# Pipeline Filters (Shared Rule)

This rule applies to **all workflows** (poetry, novel, reframe, guide). Every book pipeline passes its material through a set of **filters** — stages that shape, correct, or constrain the content before it is finalized.

## What a Filter Is

A filter is a gate that answers one question about the material and transforms it accordingly. Material is not complete until it has passed every filter in the chain.

## The Filter Chain

```
workshop → research → seeds → correctness → theme → syntax → override → quality
```

The exact filters depend on the workflow, but the principle is universal: **each filter owns a folder in the book's pipeline, and each filter reads from and writes to its own folder.**

## Filter → Folder Mapping

Every filter is backed by a folder in `.space/pipeline/book_<bookname>/filters/`. The folder is the filter's scratch space — the place where it records what it did, so the pipeline is auditable per filter.

Filter folders are **ordered and prefixed** with a number, so the chain order is visible in the filesystem:

| # | Filter | Folder | Purpose |
|---|--------|--------|---------|
| 1 | **Workshop** | `filters/1_workshop/` | Per-chapter workshop narratives — the frame (Workshop / Story / Discussion) that becomes the chapter. |
| 2 | **Research** | `filters/2_research/` | Per-chapter research — the subject, era, place, figures, and events the chapter is grounded in. |
| 3 | **Seeds** | `filters/3_seeds/` | Per-chapter character and quality seeds — who appears and what quality bar to meet. |
| 4 | **Correctness** | `filters/4_correctness/` | Fact-checking — verify every fact, term, and claim. |
| 5 | **Theme** | `filters/5_theme/` | Contemporary theme — map the timeless theme onto a present-day concern. |
| 6 | **Syntax** | `filters/6_syntax/` | Contemporary syntax — keep the prophetic voice but modernize the sentence structure. |
| 7 | **Override** | `filters/7_override/` | Human-in-the-loop — the human's `override.md` transformation. |
| 8 | **Quality** | `filters/8_quality/` | Quality review — audit against the seed analysis's quality metrics. |

All filters live under `filters/`, named `N_<name>` so the order is explicit. The novel workflow uses the first three (workshop, research, seeds); the poetry workflow uses the full set. A workflow uses the filters relevant to it, and each filter owns its folder under `filters/`.

> **Note:** the `filters/N_<name>/` folders are scaffolded by layout as the filters' scratch space. The content inside them (seeds, research notes, workshop narratives) is produced by the later workflow steps that run each filter.

## Universal Filter Principles

1. **A filter owns a folder.** Each filter reads from and writes to its own folder in the pipeline.
2. **Filters run in order.** The chain is fixed: workshop → research → seeds → correctness → theme → syntax → override → quality (or the workflow's subset).
3. **A filter is a gate.** Material is not complete until it passes every filter.
4. **Filters are auditable.** Each filter records its work in its folder, so the pipeline can be traced per filter.
5. **The human-in-the-loop is a filter, not a skill.** The human's `override.md` is applied as a filter, driven directly by the human-editable file — no skill is created for it.

## Applying the Filters

For each chapter, before marking it complete:

1. **Read the workshop** — the narrated story (or apply the poetry filters).
2. **Read the research** — the grounded subject matter.
3. **Read the seed** — who appears and the quality bar.
4. **Write the chapter** — the finished prose.

A chapter is complete only when every filter in the chain has passed.
