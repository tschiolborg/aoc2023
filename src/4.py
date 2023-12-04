from io import TextIOWrapper
import re


def compute_points(wins: int) -> int:
    return 2 ** (wins - 1)


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    res = 0

    for line in lines:
        line = line.strip()
        _, line = tuple(line.split(":"))
        correct_str, owns_str = tuple(line.strip().split("|"))

        correct: set[int] = set(re.findall(r"\d+", correct_str))
        own: set[int] = set(re.findall(r"\d+", owns_str))

        wins = len(correct.intersection(own))
        if wins > 0:
            res += compute_points(wins)

    return res


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    card_amount = {idx: 1 for idx in range(len(lines))}

    for idx, line in enumerate(lines):
        _, line_nums = tuple(line.split(":"))
        correct_str, owns_str = tuple(line_nums.strip().split("|"))

        correct: set[int] = set(re.findall(r"\d+", correct_str))
        own: set[int] = set(re.findall(r"\d+", owns_str))

        wins = len(correct.intersection(own))

        if wins > 0:
            for _ in range(card_amount[idx]):
                for i in range(wins):
                    idx_next = idx + 1 + i
                    if idx_next >= len(lines):
                        break
                    card_amount[idx + 1 + i] += 1

    return sum(card_amount.values())
