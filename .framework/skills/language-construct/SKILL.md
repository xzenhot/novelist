---
name: language-construct
description: 'Build the language layer (lexicon, register, dialect, stylistic DNA) for a book. Use when the user asks to define a language, build a vocabulary, create a dictionary, establish a register or dialect, or construct the sacred vocabulary and stylistic lexicon for a target language. Produces language/dictionary files in .space/context/references/ that the writer engine uses to render prose in the target voice.'
argument-hint: '<language> [source_text] | -o | -h'
---

# Language Construct — Lexicon & Register Engine

Builds the **language layer** for a book — the sacred vocabulary, register, dialect, and stylistic DNA that give the prose its voice in the target language. This is the "language" dimension that feeds the writer engine alongside quality (philosophy) and theme (lens).

## When to Use

- "define the language", "build a vocabulary", "create a dictionary", "construct the lexicon"
- "establish the register", "set the dialect", "what sacred words should I use"
- "build the stylistic DNA", "collect language samples"

## What a Language Construct Is

A language construct captures **how the target language should sound** — its register (archaic/literary vs. colloquial), its sacred vocabulary (the recurring lexicon), its dialect (regional forms and particles), and its stylistic DNA (signature constructions). It lives in `.space/context/references/` as a dictionary or sample file.

## The Language Layer Components

1. **Register** — the tone of the language: archaic/literary (বলিল, হইয়া, করিবার) vs. colloquial (চলতি).
2. **Sacred Vocabulary** — the recurring lexicon to weave in (e.g. অন্তরের দুর্গ, এক রক্ত, নীরব বিধান).
3. **Dialect** — regional forms, endearment particles (গো, রে, ওরে, ভাই), and grammatical variants.
4. **Stylistic DNA** — signature constructions: long flowing sentences, rich adjectives/metaphors, rhythm and euphony, profound closure.
5. **Sample Text** — a reference passage that embodies the target voice (e.g. `languages_sample.txt`).

## Commands

```
/language <language> [source_text]   # build a language construct for a target language
/language <language> -o             # show the existing language construct
/language -o | --options            # list available language constructs
/language -h | --help               # show usage
```

## Procedure

1. **Read the source** — a sample text or dictionary in `.space/context/references/` (e.g. `languages_sample.txt`, `gosai_dictionary.txt`). If none is given, ask which to use.
2. **Extract the register** — determine archaic/literary vs. colloquial, and the grammatical markers of each.
3. **Extract the sacred vocabulary** — the recurring lexicon, key terms, and signature concepts.
4. **Extract the dialect** — regional forms, endearment particles, and grammatical variants.
5. **Extract the stylistic DNA** — sentence rhythm, metaphor density, euphony, closure patterns.
6. **Write the construct** — `.space/context/references/<language>_dictionary.txt` (or a `.md`), following the components above.
7. **Register it** — add a row to `.space/context/references/registry.md`.
8. **Report** — summarize the register, sacred vocabulary, and stylistic DNA.

## Key Rules

- **One language construct = one target language/register.** Each file captures a single voice.
- **Language constructs are read-only inputs** — the writer engine reads them; it never modifies them.
- **Register is authoritative** — the `language` and `register` fields in a book's `config.json` point to the construct.
- **Sacred vocabulary is the recurring lexicon** — the words that must appear across chapters for consistency.
- **Dialect is not decoration** — it is the soul of the voice; weave in particles and regional forms deliberately.
- **Stylistic DNA drives the prose** — long flowing sentences, rich metaphor, rhythm, and profound closure.
- **A sample text anchors the voice** — include a reference passage that embodies the target style.

## References

- Sample text: [`.space/context/references/languages_sample.txt`](../../../.space/context/references/languages_sample.txt)
- Dictionary example: [`.space/context/references/gosai_dictionary.txt`](../../../.space/context/references/gosai_dictionary.txt)
- Reference registry: [`.space/context/references/registry.md`](../../../.space/context/references/registry.md)
- Themes (sacred words in context): [`.space/context/themes/gosai_bangla.md`](../../../.space/context/themes/gosai_bangla.md)
- Writer engine: [`poet` skill](../poet/SKILL.md)
