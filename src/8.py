from dataclasses import dataclass
from io import TextIOWrapper


@dataclass
class Node:
    key: str
    left: str
    right: str


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

    res = 0

    # slow

    while True:
        for s in seq:
            is_done = True
            new_nodes = []
            for node in start_nodes:
                if not node.endswith("Z"):
                    is_done = False
                if s == "L":
                    node = nodes[node].left
                else:
                    node = nodes[node].right
                new_nodes.append(node)
            if is_done:
                return res
            res += 1
            start_nodes = new_nodes
        print(res)
