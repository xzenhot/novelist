# Research Filter Summary — war / The Narrow Gate

## Run Information

- Book: `war` (The Narrow Gate)
- Form: novel
- Agent: research
- Mastery level: Experienced
- Date: 2026-09-05
- Source: `.space/backlog/epic/war/epic.md`

## What the Research Filter Did

The research filter took the 12 workshop narratives (Introduction, 1–10, Conclusion) and refined their Story sections to the target **Experienced** mastery level while preserving the Workshop and Discussion frames.

### External research attempt

- The agent attempted to use the local MCP research server via `python .tools\search-cli.py`.
- The configured backend (`searxng`) requires `SEARCHXNG_DEV_URL`/`SEARCHXNG_URL`, which is not set in this environment. A `BRAVE_API_KEY` is also not available.
- Because no external search backend is configured, grounding was verified against the existing epic, chapter models, and the workshop narratives themselves.

## Chapters Refined

| Chapter | Title | Story refinement focus |
|---|---|---|
| Introduction | The Drums Before the Rain | Tightened the "silence before the question" motif; clarified the drone-rudder attack and the global ripples from Bahrain to London. |
| 1 | The Spark in Dhow Lane | Sharpened the warning-shot skirmish, the dhow witness, and the photograph-as-causality beat; kept no killing shots. |
| 2 | Shockwaves in Markets and Capitals | Deepened the market-cyber coordination and the Amir/Maya/Moscow entanglement; emphasised *cyber closure multiplier*. |
| 3 | Asymmetric Shadows | Clarified minesweeper/destroyer imbalance, speedboat swarm, Silkworm-class coastal missile, and the rule-change beat. |
| 4 | The Ghost in the Machine | Reinforced Amir's *Narrow Gate* module as the second stage of a three-part worm; highlighted "autonomous = no one responsible". |
| 5 | The Strait Closes | Strengthened the hostage framing of *Orion Pride*, the boarding party's youth/fear, and Vance's small mercy. |
| 6 | Escalation Dominance | Tightened SEAD/HARM sequence, Okafor's ejection, and Morales's self-blame; kept mission ambiguity. |
| 7 | Behind Enemy Lines | Deepened Miller's mercy choice: three militiamen allowed to flee; kept rescue minimal and human. |
| 8 | The Human Cost on the Home Front | Centered Zahra's hospital evacuation and linked fuel riots in London/Lagos/São Paulo back to Maya's model. |
| 9 | The Decisive Battle of the Chokepoint | Clarified the layered defence geometry, Sharifi's arithmetic (run out of missiles before interceptors), and the cleared channel. |
| 10 | Dawn Over an Empty Sea | Rounded the ceasefire and survivor arcs: Lin, Zahra, Amir, Maya, Marcus, and Vance in their changed worlds. |
| Conclusion | Dawn Over an Empty Sea | Returned to the Geneva frame with the sunrise photograph and the Archivist's charge: write it as a story of people. |

## Grounding Notes Added

- **Strait of Hormuz**: described as the narrow throat, traffic separation scheme, and chokepoint for crude transit.
- **Vessels and systems**: USS Truxtun (Arleigh Burke-class destroyer), F/A-18E Super Hornet, AGM-88 HARM, SM-2 interceptors, CIWS, Seahawk helicopter, minesweeper, Silkworm-class coastal anti-ship missile, fast-attack craft (IRGCN).
- **Locations**: Strait of Hormuz, Qeshm Island, Bandar Abbas, Jebel Ali/Khalifa/Fujairah ports, Geneva archive, Bahrain Fifth Fleet HQ, London Canary Wharf, Cornwall.
- **Organisations/roles**: Fifth Fleet, National Security Council, IRGCN, SEAL CSAR team, Basij militia.
- **Cyber details**: ICS/SCADA port-management worm with a three-part chain (map dependencies → find chokepoints → trigger).

## Unresolved Grounding

Because no external search backend was reachable, the following details remain inferred from the epic/workshop and should be verified by a later filter if accuracy is critical:

- Exact current classes of Iranian fast-attack craft and coastal missile batteries.
- Precise ROE/OPORD nomenclature used by the U.S. Navy for Hormuz contingencies.
- Specific mine-countermeasures vessel classes and operating procedures.
- Detailed SEAL CSAR communication/extraction protocols.

These are marked for the **correctness** filter.

## Model Updates

All 12 chapter `model.json` files updated:
- `"state": "research"`
- `"mastery_level": "Experienced"`
- `"research_file": "chapters/<n>/chapter.md"`
- `"sources"` preserved with `.space/backlog/epic/war/epic.md`

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

## Next Filter

Run `/write war filter seeds` to continue the novel filter chain.

