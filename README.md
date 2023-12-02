My solutions to [Advent of Code](https://adventofcode.com).

* Using Python (>=3.9)
* Only python standard library, no external package
* Each solution is self contained (not using common helper functions)
* `solution_draft.ipynb` is the solution used for contest
* For some puzzles a `soultion.ipynb` exists, containing a cleaned up and commented solution
* Not highly optimized, but all solutions are finding a solution in seconds or max. some minutes.

* [2021](./2021) wip
* [2022](./2022) all finished
* [2023](./2023) ongoing

Helpfull stuff:
* Use [regular expressions](https://docs.python.org/3/library/re.html) for parsing lines
  * [`findall`](https://docs.python.org/3/library/re.html#re.findall) to get a list of matches
* Everything from `functools`, `itertools` and `collections`
* Use complex numbers and sets to represent two-dimensional grid data