from collections import Counter

DIRS = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}


def part1(s: str) -> dict:
    pos = (0, 0)
    m = Counter({pos: 1})
    for direction in s:
        dx, dy = DIRS[direction]
        x, y = pos
        pos = x + dx, y + dy
        m[pos] += 1
    return m


def part2(s: str) -> set:
    m0 = part1("".join(c for i, c in enumerate(s) if i % 2 == 0))
    m1 = part1("".join(c for i, c in enumerate(s) if i % 2 == 1))
    visited = set(m0.keys()).union(m1.keys())
    return visited
