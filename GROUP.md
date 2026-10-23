# Group submission

- Group number: CLASS
- Story: Campus Talent Show
- Group fork URL: https://github.com/mawubaskyblair-cmyk/campus-talent-show-group
- Final branch: `main`
- Deadline: Wednesday, 21 October 2026

We selected later-topic options A2, A4, and A5. 

| Member name | University access number | GitHub username | Option | Contribution | Personal branch | Merged PR link |
|---|---|---|---|---|---|---|
| Samuel | b33227 | Samuel-ahumuza | A2 | Exceptions and Safe Booking | `samuel-b33227-a2` | [#6](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/6) |
| Lawrence | b33232 | arube371 | A2 | Strict Booking Tests | `lawrence-b33232` | [#2](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/2) |
| Blair | b33217 | mawubaskyblair-cmyk | A4 | Factory and Tests | `blair-b33217` | [#7](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/7) |
| Daphine | b35639 | kasanadaphine62-glitch | A5 | Running Order Tests | `daphine-b35639` | [#8](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/8) |

## Run our work

Run these commands from the repository root on Windows:

```sh
py -3 stories/05_campus_talent_show/story.py
py -3 stories/05_campus_talent_show/demo_blair_b33217_a4.py
py -3 stories/05_campus_talent_show/demo_samuel_b33227_a2.py
py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py"