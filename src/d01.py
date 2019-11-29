# from .utils import get_input
import sys
from typing import Iterable


def climb(s: str) -> Iterable[int]:
    n = 0
    for c in s:
        if c in ("(", ")"):
            n += 1 if c == "(" else -1
            yield n


def part1(s: str) -> int:
    floor = 0
    for _floor in climb(s):
        floor = _floor
    return floor


def part2(s: str) -> int:
    for i, n in enumerate(climb(s)):
        if n < 0:
            return i + 1


def test_d01():
    tests = {
        "(())": 0,
        "()()": 0,
        "(()(()(": 3,
        "(((": 3,
        "())": -1,
        "))(": -1,
        ")())())": -3,
        ")))": -3,
    }

    for S, n in tests.items():
        assert part1(S) == n


if __name__ == "__main__":
    S = open("../data/d01.txt").read()
    print(part1(S))
    print(part2(S))
