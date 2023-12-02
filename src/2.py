import re
from io import TextIOWrapper


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    res = 0

    for idx, line in enumerate(lines):
        skip = False
        for col, num_max in (("red", 12), ("green", 13), ("blue", 14)):
            items = re.findall(rf"(\d+) {col}", line)
            if any(int(i) > num_max for i in items):
                skip = True
                continue
        if skip:
            continue

        res += idx + 1

    return res


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    res = 0

    for idx, line in enumerate(lines):
        prod = 1
        for col in ("red", "green", "blue"):
            items = re.findall(rf"(\d+) {col}", line)
            prod *= max(int(i) for i in items)

        res += prod

    return res
