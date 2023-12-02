import re
from io import TextIOWrapper


REGEX1 = r"(\d)"
REGEX2 = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"


def to_int(s):
    m = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    try:
        return int(s)
    except ValueError:
        return m[s]


def p(f: TextIOWrapper, regex: str) -> int:
    lines = f.readlines()

    sum = 0
    for line in lines:
        res = re.findall(regex, line)
        if len(res) > 0:
            a = to_int(res[0])
        else:
            continue
        if len(res) > 1:
            b = to_int(res[-1])
        else:
            b = a

        sum += a * 10 + b

    return sum


def p1(f):
    return p(f, REGEX1)


def p2(f):
    return p(f, REGEX2)
