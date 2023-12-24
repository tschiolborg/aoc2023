from dataclasses import dataclass
from io import TextIOWrapper
from math import lcm


@dataclass
class Node:
    key: str
    left: str
    right: str


@dataclass
class Pair:
    start: str
    end: str
    cycle: int


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    seq = lines[0].strip()

    lines = lines[2:]

    nodes: dict[str, Node] = {}

    for line in lines:
        line = line.strip()

        node_key, children = line.split("=")
        node_key = node_key.strip()

        children = children.replace("(", "").replace(")", "")
        left, right = children.split(",")
        left = left.strip()
        right = right.strip()

        nodes[node_key] = Node(node_key, left, right)

    res = 0

    node_key = "AAA"
    while True:
        for s in seq:
            if node_key == "ZZZ":
                return res
            if s == "L":
                node_key = nodes[node_key].left
            else:
                node_key = nodes[node_key].right
            res += 1


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    seq = lines[0].strip()

    lines = lines[2:]

    nodes: dict[str, Node] = {}

    start_nodes: list[str] = []
    end_nodes: list[str] = []

    for line in lines:
        line = line.strip()

        node, children = line.split("=")
        node = node.strip()

        children = children.replace("(", "").replace(")", "")
        left, right = children.split(",")
        left = left.strip()
        right = right.strip()

        nodes[node] = Node(node, left, right)

        if node.endswith("A"):
            start_nodes.append(node)
        elif node.endswith("Z"):
            end_nodes.append(node)

    end_set = set(end_nodes)
    pairs: list[Pair] = []

    for node in start_nodes:
        found_cycle = False
        end = None
        cycle = 0
        while True:
            if found_cycle:
                break

            for s in seq:
                if end is not None:
                    cycle += 1
                if end is not None and node == end:
                    found_cycle = True
                    pairs.append(Pair(node, end, cycle))
                    break
                if node in end_set:
                    end_set.discard(node)
                    end = node
                if s == "L":
                    node = nodes[node].left
                else:
                    node = nodes[node].right

    return lcm(*(pair.cycle for pair in pairs))
