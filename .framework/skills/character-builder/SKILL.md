---
name: character-builder
description: 'Build and manage characters for novels. Use when the user asks to create characters, build a character list, add characters to a novel, flesh out a character, or populate characters.json for a novel. Produces the characters.json schema (all_characters with identity and personality_traits) for a novel pipeline.'
argument-hint: '<bookname> [character_name...] | -o | -h'
---

# Character Builder — Novel Character Engine

Builds and maintains the character roster for a frame-story novel. Every character is recorded in the novel's `characters.json` so the writing engine can draw on them consistently across chapters.

## When to Use

- "create characters", "build characters", "add a character", "flesh out a character"
- "populate characters.json", "who are the characters", "list characters"
- "add 3-5 new characters for chapter N"

## The Character Schema

Characters live in `.space/pipeline/book_<bookname>/characters.json`, shaped as:

```json
{
  "all_characters": [
    {
      "character_id": 1,
      "friendly_name": "বল্লাল সেন",
      "identity": {
        "name": "বল্লাল সেন (Ballal Sen)",
        "title": "গৌড়েশ্বর, অরিরাজ-নিঃশঙ্ক-শঙ্কর",
        "age": 62,
        "sex": "পুরুষ",
        "caste": "ব্রহ্ম-ক্ষত্রিয় (সেন বংশ)",
        "occupation": "বাংলার অধিপতি ও সমাজ সংস্কারক"
      },
      "personality_traits": {
        "intellect": "স্মৃতিশাস্ত্র ও জ্যোতিষবিদ্যায় প্রগাঢ় পাণ্ডিত্যের অধিকারী।",
        "motivation": "বাঙালি সমাজকে বৈদিক ও পৌরাণিক স্মৃতি-সংস্কৃতির মাধ্যমে ঢেলে সাজানো।"
      }
    }
  ]
}
```

### Field Reference

| Field | Meaning |
|-------|---------|
| `character_id` | Sequential integer, unique per character. |
| `friendly_name` | The short name used in dialogue and chapter seeds. |
| `identity.name` | Full name (optionally with transliteration). |
| `identity.title` | Honorific, rank, or epithet. |
| `identity.age` | Age (number) — optional. |
| `identity.sex` | পুরুষ / নারী. |
| `identity.caste` | Caste, clan, or lineage — optional. |
| `identity.occupation` | Role, profession, or station. |
| `personality_traits` | Free-form key→value map: strengths, weaknesses, motivation, mood, intellect, etc. |

## Commands

```
/character <bookname> [character_name...]   # build/add characters for a novel
/character <bookname> -o | --options       # list existing characters
/character -h | --help                     # show usage
```

## Procedure

1. **Locate the novel** — `.space/pipeline/book_<bookname>/characters.json`. If it does not exist, the novel's layout has not been scaffolded yet; run the `novelist` skill first (`/novel <bookname> <chapter_count>`).
2. **Read existing characters** — load `characters.json` to avoid duplicates and to assign the next `character_id`.
3. **Build each character** — for each requested name, fill `identity` and `personality_traits`:
   - **Real (historical) characters** — ground them in the source material; cite references where available.
   - **Fictional characters** — invent them to serve the story (warrior, princess, minister, poet, merchant, priest, commoner).
4. **Write back** — append new characters to `all_characters`, preserving existing ones, and save `characters.json`.
5. **Report** — list added characters and the new total count.

## Key Rules

- **`characters.json` is the single source of truth** for the novel's cast. The writing engine reads it for every chapter.
- **Never overwrite** — append new characters; preserve existing `character_id`s.
- **`character_id` is sequential** — assign the next unused integer.
- **Mix real and fictional** — historical novels blend documented figures with invented ones; mark fictional characters clearly in `occupation` or a note.
- **3–5 new characters per chapter** is the convention for the frame-story engine — build the roster ahead of the chapters that use them.
- **`friendly_name` is what dialogue uses** — keep it short and natural.

## References

- Canonical example: [`.space/pipeline/book_laxman/characters.json`](../../../.space/pipeline/book_laxman/characters.json)
- Novel layout & engine: [`novelist` skill](../novelist/SKILL.md) and [`.framework/workflows/novel.md`](../../../.framework/workflows/novel.md)
