from typing import List, Sequence, Tuple, Optional

VOWELS = 'aeiou'

def has_at_least_three_vowels(s: str) -> bool:
    return sum(1 for c in s if c in VOWELS) >= 3

def has_repeat_char(s: str) -> bool:
    return any(c1 == c2 for c1, c2 in zip(s, s[1:]))

def no_blacklist(s: str) -> bool:
    for x in ('ab', 'cd', 'pq', 'xy',):
        if x in s:
            return False
    return True


def is_nice(s: str) -> bool:
    s = s.lower().strip()
    return has_at_least_three_vowels(s) and has_repeat_char(s) and no_blacklist(s)

def part1(lines: Sequence[str]) -> int:
    return sum(1 for line in lines if is_nice(line))


def has_non_overlap_repeat(s) -> bool:
    from textwrap import wrap
    from collections import Counter

    # look for chunks of size 2 starting from an even offset (n0) and an odd offset (n1)
    [(_, n0)] = Counter(x for x in wrap(s, 2) if len(x) == 2).most_common(1)
    [(_, n1)] = Counter(x for x in wrap(s[1:], 2) if len(x) == 2).most_common(1)
    return n0 >= 2 or n1 >= 2

def non_overlap_repeat(s: str) -> Optional[Tuple[str, Tuple[int,int]]]:
    L = len(s)
    for i in range(L - 3):
        l_pair = s[i:i+2]
        for j in range(i + 2, L - 1):
            if l_pair == s[j:j+2]:
                return l_pair, (i, j)
    return None


def xyx(s: str) -> bool:
    return any(c0 == c2 for c0, c2 in zip(s, s[2:]))


def test_non_overlap_repeat():
    assert non_overlap_repeat('aaa') is None
    assert non_overlap_repeat('aaaa') == 'aa', (0,2)
    assert non_overlap_repeat('bcdfacd') == 'cd', (1,5)


def part2(lines: Sequence[str]) -> int:
    return sum(1 for line in lines if xyx(line) and non_overlap_repeat(line))


if __name__ == '__main__':
    with open('../data/d05.txt') as fp:
        lines = tuple(line.strip().lower() for line in fp)
        print(part1(lines))
