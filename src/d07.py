import re
from collections import deque

from typing import Dict, Set, Tuple


def edges(s: str) -> Tuple[str]:
    return tuple(nbr for nbr in s.split() if nbr.islower())


def parse():
    import re

    rgx = re.compile(r"^([ a-zA-Z0-9]+) -> ([a-z]+)$")

    with open("/home/dmb/aoc/data/d07.txt") as fp:
        lines = tuple(x.strip() for x in fp)

    return {
        gate: action for action, gate in (rgx.match(line).groups() for line in lines)
    }


def topological(G: Dict[str, str]):
    G = {
        gate: set(x for x in action.split() if x.islower())
        for gate, action in G.items()
    }
    visited = dict()

    for i in range(len(G)):
        loop_seen = set()

        for node, dependencies in G.items():
            if node in visited:
                continue

            if all(d in visited for d in dependencies):
                loop_seen.add(node)

        for node in loop_seen:
            visited[node] = i

    return visited


def by_levels(G: Dict[str, str]) -> Dict[int, Set[str]]:
    from collections import defaultdict
    M = defaultdict(set)
    for node, level in topological(G).items():
        M[level].add(node)
    return M


def closure(G: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    marked = set()
    Q = deque(['a'])
    while Q:
        node = Q.popleft()
        for nbr in G[node]:
            if nbr in marked:
                continue
            Q.append(nbr)
            marked.add(nbr)
    return {
        k: v for k, v in G.items() if k in marked
    }


def eval_expr(s: str, scope: Dict[str, int]) -> int:
    if s.isdigit():
        return int(s)

    if s.isalpha():
        return scope[s]

    if m := re.match(r'^NOT ([a-z]+)$', s):
        symbol = m.group(1)
        val = scope[symbol]
        assert isinstance(val, int)
        return ~val

    if m := re.match(r'^([0-9]+|[a-z]+) (AND|OR|RSHIFT|LSHIFT) ([0-9]+|[a-z]+)$', s):
        left, op, right = m.groups()
        left = int(left) if left.isdigit() else scope[left]
        right = int(right) if right.isdigit() else scope[right]
        op = {
            "AND": lambda x, y: x & y,
            "OR": lambda x, y: x | y,
            "LSHIFT": lambda x, y: x << y,
            "RSHIFT": lambda x, y: x >> y,
        }[op]
        return op(left, right)

    breakpoint()
    assert False, (s, scope)


def evaluate(G: Dict[str, str]) -> Dict[str, int]:
    scope = {}
    for level, nodes in by_levels(G).items():
        for node in nodes:
            expr = G[node]
            scope[node] = eval_expr(expr, scope)
    return scope


def part2(G: Dict[str, str]) -> Dict[str, int]:
    part1 = evaluate(G)
    return evaluate({
        **G, 'b': str(part1['a'])
    })
