import argparse
from importlib import import_module


def run(func, filename):
    with open(filename) as f:
        print(func(f))
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2020")
    parser.add_argument("day", type=int, help="Day to run")
    parser.add_argument("part", type=int, help="Part to run")

    args = parser.parse_args()

    day: int = args.day
    part: int = args.part

    module = import_module(f"src.{day}")

    func = getattr(module, f"p{part}", None)
    if func is None:
        raise ValueError(f"Day {args.day} does not have part {part}")

    # print("test:")
    # run(func, f"data/{day}.test{part}")

    # print("input:")
    run(func, f"data/{args.day}.in")
