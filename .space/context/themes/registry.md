# Theme Registry

A catalog of every thematic category set available in `context/themes/`. Each theme file defines the philosophical lenses that give chapters their spine — the categories the writer agent cycles through when assigning a lens to each term from the index.

The writer agent reads this registry to discover available theme sets, then reads the individual theme file for the full definitions.

---

## Available Theme Sets

| # | Theme File | Source | Theme Count | Language | Status |
|---|-----------|--------|-------------|----------|--------|
| 1 | [`generic.md`](generic.md) | Marcus Aurelius — *The Meditations* | 10 | Target language | ✅ Active |

---

## Theme Set Details

### 1. `generic.md` — The Ten Stoic Themes

- **Source:** Marcus Aurelius's *Meditations* (Stoic philosophy)
- **Theme Count:** 10
- **Language:** Target language — archaic/literary register
- **Associated Quality:** [`../qualities/aurilus.md`](../qualities/aurilus.md)
- **Associated Index:** `bookseed.txt` (topics/terms in the target language)

**The Ten Themes:**`r`n`r`n| # | Theme | Essence | Notes |
|---|-------|---------|-------|
| 1 | The Inner Citadel | Withdrawal into the self as an unbreachable refuge | Use the target-language equivalent at generation time. |
| 2 | The One Blood | Universal kinship; all beings as limbs of one body | Use the target-language equivalent at generation time. |
| 3 | The Fading Name | Indifference to fame; the vanity of reputation | Use the target-language equivalent at generation time. |
| 4 | The Only Present | The eternal now; past and future as ghosts | Use the target-language equivalent at generation time. |
| 5 | The Beloved Necessity | Amor fati — loving one's fate | Use the target-language equivalent at generation time. |
| 6 | The Last Change | Death as transformation, not ending | Use the target-language equivalent at generation time. |
| 7 | The Royal Service | Service as the highest nobility | Use the target-language equivalent at generation time. |
| 8 | The Uncluttered Soul | Simplicity and detachment | Use the target-language equivalent at generation time. |
| 9 | The Woven Whole | The unity of all things | Use the target-language equivalent at generation time. |
| 10 | The Undefeated Virtue | Virtue's invincibility | Use the target-language equivalent at generation time. |

Each theme in `generic.md` provides: **essence**, **Stoic source** (the grounding quote), **Gibran transformation** (how to render it prophetically), **metaphor family** (imagery to draw from), **sacred words** (the target-language lexicon), and a **sample opening** (a ready-made "The Question" line).

---

## How to Add a New Theme Set

1. Create a new theme file in `context/themes/` (e.g. `rumi.md`, `tagore.md`, `nietzsche.md`).
2. Follow the same structure as `generic.md`:
   - A title and one-line description
   - A numbered list of themes, each with:
     - **Essence** (one-line core)
     - **Source** (the grounding quote from the reference work)
     - **Transformation** (how to render it prophetically)
     - **Metaphor Family** (imagery to draw from)
     - **Sacred Words** (the target-language lexicon)
     - **Sample Opening** (a ready-made "The Question" line)
   - A "Usage Notes" section (cycling, weaving, grounding, one-theme-per-chapter)
3. Add a row to the table above and a detail section below.
4. Point a book instance (`writer.md`) at the new theme set.

---

## Conventions

- **One theme set = one philosophical source.** Each file derives its themes from a single reference work.
- **Theme files are read-only inputs.** The writer agent reads them; it never modifies them.
- **Themes are distinct from qualities.** A quality (`context/qualities/`) defines *how* to write (voice, metaphor families, quality metrics); a theme set (`context/themes/`) defines *what lens* to apply to each chapter.
- **Cycle in order.** The writer assigns themes by cycling through the list (1 → N → 1) so no theme dominates.

