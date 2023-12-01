import re
import os


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


def main():
    path = os.path.join(os.path.dirname(__file__), "data")
    path_in = os.path.join(path, "1.in")
    path_out = os.path.join(path, "1.out")

    with open(path_in, "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        res = re.findall(REGEX2, line)
        if len(res) > 0:
            a = to_int(res[0])
        else:
            continue
        if len(res) > 1:
            b = to_int(res[-1])
        else:
            b = a

        sum += a * 10 + b

    with open(path_out, "w") as f:
        f.write(str(sum) + "\n")


if __name__ == "__main__":
    main()
