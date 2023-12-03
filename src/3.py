from io import TextIOWrapper


def is_symbol(c: str) -> bool:
    return c != "." and c != "\n" and not c.isnumeric()


def is_gear(c: str) -> bool:
    return c == "*"


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    res = 0

    n = len(lines)
    m = len(lines[0])

    for i, line in enumerate(lines):
        num = ""
        is_part = False
        for j, c in enumerate(line):
            if c.isnumeric():
                num += c
                if i > 0 and is_symbol(lines[i - 1][j]):
                    is_part = True
                elif i > 0 and j > 0 and is_symbol(lines[i - 1][j - 1]):
                    is_part = True
                elif i > 0 and j < m - 1 and is_symbol(lines[i - 1][j + 1]):
                    is_part = True
                elif j > 0 and is_symbol(lines[i][j - 1]):
                    is_part = True
                elif j < m - 1 and is_symbol(lines[i][j + 1]):
                    is_part = True
                elif i < n - 1 and is_symbol(lines[i + 1][j]):
                    is_part = True
                elif i < n - 1 and j > 0 and is_symbol(lines[i + 1][j - 1]):
                    is_part = True
                elif i < n - 1 and j < m - 1 and is_symbol(lines[i + 1][j + 1]):
                    is_part = True
            else:
                if num and is_part:
                    res += int(num)
                num = ""
                is_part = False

    return res


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    res = 0

    n = len(lines)
    m = len(lines[0])

    gears: dict[tuple[int, int], list[int]] = dict()  # (i, j) -> [num, num]

    for i, line in enumerate(lines):
        num = ""
        gear_coords: set[tuple[int, int]] = set()
        for j, c in enumerate(line):
            if c.isnumeric():
                num += c
                if i > 0 and is_gear(lines[i - 1][j]):
                    gear_coords.add((i - 1, j))
                elif i > 0 and j > 0 and is_gear(lines[i - 1][j - 1]):
                    gear_coords.add((i - 1, j - 1))
                elif i > 0 and j < m - 1 and is_gear(lines[i - 1][j + 1]):
                    gear_coords.add((i - 1, j + 1))
                elif j > 0 and is_gear(lines[i][j - 1]):
                    gear_coords.add((i, j - 1))
                elif j < m - 1 and is_gear(lines[i][j + 1]):
                    gear_coords.add((i, j + 1))
                elif i < n - 1 and is_gear(lines[i + 1][j]):
                    gear_coords.add((i + 1, j))
                elif i < n - 1 and j > 0 and is_gear(lines[i + 1][j - 1]):
                    gear_coords.add((i + 1, j - 1))
                elif i < n - 1 and j < m - 1 and is_gear(lines[i + 1][j + 1]):
                    gear_coords.add((i + 1, j + 1))
            else:
                if num and gear_coords:
                    for coord in gear_coords:
                        gears.setdefault(coord, [])
                        gears[coord].append(int(num))
                num = ""
                gear_coords = set()

    for nums in gears.values():
        if len(nums) == 2:
            res += nums[0] * nums[1]

    return res
