import re
from typing import Tuple, Iterable, Callable, Dict

Point = Tuple[int, int]


def points(p0: Point, p1: Point) -> Iterable[Point]:
    ((x0, y0), (x1, y1)) = p0, p1
    return ((x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1))


ACTIONS = {
    "part1": {
        "turn on": lambda _: 1,
        "turn off": lambda _: 0,
        "toggle": lambda x: x ^ 1,
    },
    "part2": {
        "turn on": lambda x: x + 1,
        "turn off": lambda x: max(x - 1, 0),
        "toggle": lambda x: x + 2,
    },
}


def parse(line: str, actions: Dict[str, Callable]) -> Tuple[Callable, Point, Point]:
    rgx = re.compile(r"(^turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")
    action, x0, y0, x1, y1 = rgx.match(line.strip()).groups()
    action = actions[action]
    return action, (int(x0), int(y0)), (int(x1), int(y1))


def interpret(lines: Tuple[str], actions: Dict[str, Callable]) -> int:
    m = {p: 0 for p in points((0, 0), (999, 999))}

    for line in lines:
        f, p0, p1 = parse(line, actions)
        for p in points(p0, p1):
            m[p] = f(m[p])

    return sum(m.values())


def main():
    with open("/home/dmb/aoc/data/d06.txt") as fp:
        lines = tuple(x.strip().lower() for x in fp)
        for i in (1, 2):
            print(i, interpret(lines, ACTIONS[f"part{i}"]))


if __name__ == "__main__":
    main()
