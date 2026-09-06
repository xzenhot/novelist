# Override Command File - Dolly

You are the human-in-the-loop agent of the poetry pipeline. This command file applies to every poem in .space/pipeline/book_dolly/bookseed.txt, each structured as Question / Oration / Benediction.

The override is a human-editable transformation layer. Write instructions below the --- line to transform every poem, or scope an instruction to a specific poem number.

Command file path: .space/pipeline/book_dolly/filters/override/filter.md
Model update paths: .space/pipeline/book_dolly/chapters/<n>/model.json
Backlog planning copy: .space/backlog/epic/dolly/override.md

## Context Summary

| # | Poem Topic | Subject | Theme | Stereotype |
|---|---|---|---|---|
| 1 | First Sight In New Delhi | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 2 | Radha By The Yamuna | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 3 | The Pitcher In Her Lap | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 4 | City Dust And River Light | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 5 | The Ethics Of Praise | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 6 | A Lovable Distance | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 7 | Balcony At Evening | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 8 | Clay, Water, And Name | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 9 | The Poet's Restlessness | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 10 | Dolly's Human Radiance | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 11 | The Yamuna Within | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 12 | Benediction For Dolly | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 13 | Metro Windows At Dusk | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 14 | The Anklet Of Traffic | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 15 | A Blue Sari In Memory | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 16 | The Unsaid Greeting | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 17 | Pitcher As Moon | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 18 | Braj In The Capital | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 19 | The Beloved's Autonomy | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 20 | Jasmine Near The Road | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 21 | Question Before Beauty | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 22 | The Hand That Holds Water | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 23 | Delhi Heat, Yamuna Memory | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 24 | The Flute Not Heard | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 25 | Prayer Without Temple | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 26 | Radha's Shadow, Dolly's Face | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 27 | The Poet's Shame | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 28 | Water At The Edge Of Speech | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 29 | A Name Written In Air | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 30 | Evening Lamps Of Delhi | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 31 | The River's Polluted Mirror | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 32 | Beauty And Responsibility | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 33 | The Clay Maker's Lesson | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 34 | Monsoon Over New Delhi | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 35 | Distance As Devotion | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 36 | Dolly In The Market Light | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 37 | A Dupatta Like Water | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 38 | The Threshold | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 39 | What The Pitcher Carries | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 40 | The Poet's Discipline | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 41 | Radha Beyond Ornament | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 42 | Dolly Beyond Comparison | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 43 | Yamuna At Night | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 44 | The City As Witness | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 45 | The Beloved's Laughter | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 46 | The Weight Of The Pitcher | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 47 | A River Under Asphalt | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 48 | The Poet's Jealousy | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 49 | The Garland Refused | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 50 | Sacred Ordinary Morning | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 51 | The Gaze Washed Clean | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 52 | The Pitcher Returned To Earth | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 53 | Dolly's Silence | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 54 | The Poet's Inner Vrindavan | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 55 | A Blessing At The Riverbank | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 56 | The Last Question Of Desire | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 57 | Yamuna Of The Heart | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 58 | Dolly Free In Delhi | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 59 | Song Without Possession | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |
| 60 | Final Benediction | philosophical devotional love poetry | pending theme | rabindrasangeet / gosai_bangla |

---

## Instructions

