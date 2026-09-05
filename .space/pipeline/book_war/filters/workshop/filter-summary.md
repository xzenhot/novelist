# Workshop Filter Summary — war / The Narrow Gate

## Run Information

- Book: `war` (The Narrow Gate)
- Form: novel
- Agent: workshop
- Date: 2026-09-05
- Source: `.space/backlog/epic/war/epic.md`

## Chapters Produced

| Order | Chapter | Title | Primary POV / Figures | Narrative Handoff |
|---|---|---|---|---|
| 0 | Introduction | The Drums Before the Rain | Commander Sarah Lin, Captain Reza Sharifi | Tanker explosion closes the strait; frame sets the next drum: money. |
| 1 | 1 | The Spark in Dhow Lane | Sarah Lin, Reza Sharifi | Skirmishes begin; no killing shots, but the world tilts on images and lies. |
| 2 | 2 | Shockwaves in Markets and Capitals | Dr. Maya Thorne, Marcus Vance, Amir | Oil spike and UAE port cyberattack reveal a coordinated escalation. |
| 3 | 3 | Asymmetric Shadows | Sarah Lin, Reza Sharifi | Speedboat swarm and coastal missile attack; mines remain in the water. |
| 4 | 4 | The Ghost in the Machine | Amir | Amir discovers his own code became the weapon; sends a message to London. |
| 5 | 5 | The Strait Closes | Captain Thomas Vance, Sarah Lin | Iran closes the strait; Orion Pride becomes a hostage. |
| 6 | 6 | Escalation Dominance | Viper Morales | SEAD mission succeeds; wingman Okafor is shot down. |
| 7 | 7 | Behind Enemy Lines | Master Chief Miller, Okafor | SEAL rescue; three militiamen allowed to live. |
| 8 | 8 | The Human Cost on the Home Front | Zahra, Maya Thorne | Hospital evacuation and global fuel riots. |
| 9 | 9 | The Decisive Battle of the Chokepoint | Sarah Lin, Reza Sharifi | Coalition clears a channel; missiles and boats run out before will does. |
| 10 | 10 | Dawn Over an Empty Sea | Sarah Lin, Zahra, Amir, Maya Thorne, Marcus Vance | Fragile ceasefire; the gate reopens but the peace is conditional. |
| 11 | Conclusion | Dawn Over an Empty Sea | Sarah Lin, Zahra, Amir, Maya Thorne | Frame returns; Archivist charges the correspondent to write it as a story of people. |

## Frame Characters

- **The Archivist** — older historian/guide working from a Geneva archive. She selects artefacts, interprets silence, and bridges each chapter to the next.
- **The Young Correspondent** — sceptical journalist writing an article. He asks the questions the reader would ask and receives thematic answers.

## Common Frame Devices

- Each chapter opens with a physical artefact (thumb drive, photograph, chart, helmet, notebook, register, radar printout, sunrise photograph).
- The frame transitions from modern analysis into the historical/geopolitical story, then returns to a discussion that names the next chapter's drumbeat.

## Narrative Arc Across Chapters

1. **Silence before war** (Introduction) → the unasked question.
2. **The spark** (1) → images and lies begin to tilt reality.
3. **Economic escalation** (2) → oil and cyber reveal coordination.
4. **Asymmetric naval warfare** (3) → cheap threats vs. expensive ships.
5. **Cyber confessional** (4) → the weapon escapes its maker.
6. **Closure and hostage-taking** (5) → civilians become bargaining chips.
7. **Air war and loss** (6) → a pilot is lost, a commander blames himself.
8. **Rescue and mercy** (7) → mercy in enemy territory.
9. **Civilian cost** (8) → the war leaves the battlefield.
10. **Decisive engagement** (9) → machines run out of missiles.
11. **Conditional peace** (10 + Conclusion) → no winners, only survivors.

## Notes for the Next Filter

- The research filter should verify: Hormuz geography and shipping-lane separation scheme; classes of minesweepers and anti-ship missiles; F/A-18E SEAD/HARM operations; Iranian fast-attack craft (IRGCN); SEAL CSAR procedures; Bandar Abbas hospital infrastructure; oil-market futures mechanics; cyber-worm attack patterns on ICS/SCADA.
- The seeds filter should assign included characters per chapter, confirm mood and stereotype (`gibran`), and ensure target word count (4,500) is respected in later prose writing.
- Current chapter state is `workshop` across all 12 chapters. The next filter should update state to `research` and set `research_file` after validation.

## Output Files

- `.space/pipeline/book_war/chapters/Introduction/chapter.md`
- `.space/pipeline/book_war/chapters/1/chapter.md`
- `.space/pipeline/book_war/chapters/2/chapter.md`
- `.space/pipeline/book_war/chapters/3/chapter.md`
- `.space/pipeline/book_war/chapters/4/chapter.md`
- `.space/pipeline/book_war/chapters/5/chapter.md`
- `.space/pipeline/book_war/chapters/6/chapter.md`
- `.space/pipeline/book_war/chapters/7/chapter.md`
- `.space/pipeline/book_war/chapters/8/chapter.md`
- `.space/pipeline/book_war/chapters/9/chapter.md`
- `.space/pipeline/book_war/chapters/10/chapter.md`
- `.space/pipeline/book_war/chapters/Conclusion/chapter.md`

Each matching `.space/pipeline/book_war/chapters/<n>/model.json` updated to:
- `"state": "workshop"`
- `"workshop_file": "chapters/<n>/chapter.md"`

