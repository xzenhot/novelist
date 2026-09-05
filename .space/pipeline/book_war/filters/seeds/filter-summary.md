# Seeds Filter Summary — war / The Narrow Gate

## Run Information

- Book: `war` (The Narrow Gate)
- Form: novel
- Agent: seeds
- Date: 2026-09-05
- Source: `.space/backlog/epic/war/epic.md`

## What the Seeds Filter Did

The seeds filter curated each chapter's seed text, selected its included characters, set a shared quality bar, and ensured the segment structure exists for the upcoming prose-writing phase.

Each chapter is treated as a single segment (`segments/1`) matching the workshop/research chapter-unit already in place.

## Chapter Seed Table

| Chapter | Title | Characters | Seed focus |
|---|---|---|---|
| Introduction | The Drums Before the Rain | Sarah Lin, Reza Sharifi, Marcus Vance, Maya Thorne | The fragile morning calm across the strait; the explosion seen from both shores and from trading floors; no single decision starts the fire. |
| 1 | The Spark in Dhow Lane | Sarah Lin, Reza Sharifi | The Panama Crown listing in the narrow throat; warning shots and the first propaganda photograph. |
| 2 | Shockwaves in Markets and Capitals | Maya Thorne, Marcus Vance, Amir | Market panic, NSC paralysis, and the first SCADA anomalies that signal the cyber dimension. |
| 3 | Asymmetric Shadows | Sarah Lin, Reza Sharifi, Master Chief Miller | Minesweepers vs. speedboat swarms and coastal missiles; the weak change the rules. |
| 4 | The Ghost in the Machine | Amir, Zahra | Amir traces NARROW GATE and recognizes his own code; Zahra's hospital shift makes the cost intimate. |
| 5 | The Strait Closes | Sarah Lin, Reza Sharifi, Thomas Vance | Iran closes the strait; trapped tankers and a small mercy shown by Captain Vance. |
| 6 | Escalation Dominance | Viper Morales, Sarah Lin | Operation Open Gate launches; SEAD strike and Okafor's ejection at sunrise. |
| 7 | Behind Enemy Lines | Master Chief Miller, Viper Morales, Zahra | SEAL rescue through coastal villages; Miller's mercy choice; extraction under fire. |
| 8 | The Human Cost on the Home Front | Zahra, Maya Thorne | Bandar Abbas hospital evacuation; fuel riots in London, Lagos, and São Paulo. |
| 9 | The Decisive Battle of the Chokepoint | Sarah Lin, Reza Sharifi, Viper Morales | Layered strait-clearing battle; a contest of exhaustion and dwindling reasons to fight. |
| 10 | Dawn Over an Empty Sea | Sarah Lin, Reza Sharifi, Zahra, Maya Thorne, Amir, Thomas Vance, Viper Morales | Ceasefire, aftermath, and the question of whether the world has learned anything. |
| Conclusion | Dawn Over an Empty Sea | Sarah Lin, Zahra, Maya Thorne, Reza Sharifi, Thomas Vance | Geneva archive frame closes; the Archivist asks the Correspondent to write the people, not the fleets. |

## Included Characters Format

Each chapter `model.json` now contains `included_characters` as an array of:
```json
{
  "character_id": "sarah_lin",
  "full_name": "Commander Sarah Lin",
  "role_in_chapter": "Executive Officer of the USS Truxtun"
}
```

Characters are drawn exclusively from `characters.json`; no new characters were invented.

## Quality Parameters Set

All chapters share the same quality bar:
- **register**: geopolitical thriller
- **tone**: tense, grounded, cinematic
- **language**: English
- **target_word_count**: 4500
- **philosophical_depth**: explore the illusion of control and the distance between decision-makers and sufferers
- **metaphorical_richness**: use sea, gate, fire, and machine imagery consistently
- **accessibility**: clear to adult thriller readers without military background
- **resonance**: human cost of systemic violence
- **timelessness**: echo classical questions of responsibility and mercy

## Segment Layout

For every chapter:
- `.space/pipeline/book_war/chapters/<n>/segments/1/`
- `.space/pipeline/book_war/chapters/<n>/segments/1/writer/`
- `.space/pipeline/book_war/chapters/<n>/segments/1/editor/`
- `.space/pipeline/book_war/chapters/<n>/segments/1/translator/`
- `.space/pipeline/book_war/chapters/<n>/segments/1/model.json` with `level: "segment"`, `state: "seeds"`, `segment_index: 1`

## Model Updates

All 12 chapter `model.json` files updated:
- `"state": "seeds"`
- `"chapter_title"`: set per chapter
- `"chapter_summary"`: rich seed text shaped by epic and mood
- `"included_characters"`: roster drawn from `characters.json`
- `"quality_parameters"`: shared quality bar
- `"segments": [1]`
- `"mood"`: preserved or defaulted

## Output Files

Chapter models:
- `.space/pipeline/book_war/chapters/Introduction/model.json`
- `.space/pipeline/book_war/chapters/1/model.json`
- `.space/pipeline/book_war/chapters/2/model.json`
- `.space/pipeline/book_war/chapters/3/model.json`
- `.space/pipeline/book_war/chapters/4/model.json`
- `.space/pipeline/book_war/chapters/5/model.json`
- `.space/pipeline/book_war/chapters/6/model.json`
- `.space/pipeline/book_war/chapters/7/model.json`
- `.space/pipeline/book_war/chapters/8/model.json`
- `.space/pipeline/book_war/chapters/9/model.json`
- `.space/pipeline/book_war/chapters/10/model.json`
- `.space/pipeline/book_war/chapters/Conclusion/model.json`

Segment models:
- `.space/pipeline/book_war/chapters/<n>/segments/1/model.json` (all 12 chapters)

## Next Filter

Run `/write war filter correctness` to continue the novel filter chain.

