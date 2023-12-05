from dataclasses import dataclass
from io import TextIOWrapper
import re
from math import inf


@dataclass
class Range:
    destination: int
    source: int
    length: int


@dataclass
class SeedRange:
    start: int
    length: int


def find_ints(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", line)))


def find_range(line: str) -> Range:
    ints = find_ints(line)
    return Range(destination=ints[0], source=ints[1], length=ints[2])


def construct_map_func(seed_to_soils: list[Range]):
    def func(x: int) -> int:
        for seed_to_soil in seed_to_soils:
            if seed_to_soil.source <= x < seed_to_soil.source + seed_to_soil.length:
                return seed_to_soil.destination + x - seed_to_soil.source
        return x

    return func


def get_seed_range(line: str) -> list[SeedRange]:
    ints = find_ints(line)
    items = []
    for i in range(0, len(ints), 2):
        items.append(SeedRange(start=ints[i], length=ints[i + 1]))

    return items


def p1(f: TextIOWrapper) -> int:
    lines = iter(f)
    line = next(lines)

    seeds = find_ints(line)

    next(lines)

    map_funcs = []

    for i in range(7):
        next(lines)  # map name line

        seed_to_soils = []
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
            if line.strip() == "":
                break

            seed_to_soils.append(find_range(line))

        map_funcs.append(construct_map_func(seed_to_soils))

    res = inf
    for x in seeds:
        for map_func in map_funcs:
            x = map_func(x)
        if x < res:
            res = x

    return res


def p2(f: TextIOWrapper) -> int:
    lines = iter(f)
    line = next(lines)

    # this is correct, but not optimal -> very slow

    seeds_ranges = get_seed_range(line)

    next(lines)

    map_funcs = []

    for i in range(7):
        next(lines)  # map name line

        seed_to_soils = []
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
            if line.strip() == "":
                break

            seed_to_soils.append(find_range(line))

        map_funcs.append(construct_map_func(seed_to_soils))

    res = inf
    for seed_range in seeds_ranges:
        for x in range(seed_range.start, seed_range.start + seed_range.length):
            for map_func in map_funcs:
                x = map_func(x)
            if x < res:
                res = x

    return res
