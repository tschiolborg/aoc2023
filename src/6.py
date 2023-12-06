from io import TextIOWrapper
import re


def get_ints(line: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", line)]


def get_int(line: str) -> int:
    return int("".join(re.findall(r"\d+", line)))


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    times = get_ints(lines[0])
    dists = get_ints(lines[1])

    res = 1
    for t, d in zip(times, dists):
        c = 0
        for i in range(t + 1):
            if (t - i) * i > d:
                c += 1
        res *= c

    return res


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    time = get_int(lines[0])
    dist = get_int(lines[1])

    res = 0
    for i in range(time + 1):
        if (time - i) * i > dist:
            res += 1

    return res
