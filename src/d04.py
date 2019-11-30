from hashlib import md5
from itertools import count


def digest(x: str) -> str:
    return md5(x.encode("utf-8")).hexdigest()


def part1(key: str, difficulty=5) -> int:
    for n in count():
        if digest(f"{key}{n}").startswith("0" * difficulty):
            return n


KEY = "iwrupvqb"

if __name__ == "__main__":
    print(part1(key=KEY))
    print(part1(key=KEY, difficulty=6))
