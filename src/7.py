from io import TextIOWrapper


def five(cards: str) -> bool:
    return len(set(cards)) == 1


def four(cards: str) -> bool:
    return len(set(cards)) == 2 and (
        cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4
    )


def full_house(cards: str) -> bool:
    return len(set(cards)) == 2 and (
        cards.count(cards[0]) == 3
        or cards.count(cards[1]) == 3
        or cards.count(cards[2]) == 3
    )


def three(cards: str) -> bool:
    return len(set(cards)) == 3 and (
        cards.count(cards[0]) == 3
        or cards.count(cards[1]) == 3
        or cards.count(cards[2]) == 3
    )


def two_pair(cards: str) -> bool:
    return len(set(cards)) == 3 and (
        cards.count(cards[0]) == 2
        or cards.count(cards[1]) == 2
        or cards.count(cards[2]) == 2
    )


def one_pair(cards: str) -> bool:
    return len(set(cards)) == 4


def high_card(cards: str) -> bool:
    return len(set(cards)) == 5


def determine_type(cards: str, func) -> bool:
    if "1" in cards:
        for c in ["E", "D", "C", "A", "9", "8", "7", "6", "5", "4", "3", "2"]:
            if func(cards.replace("1", c)):
                return True
        return False
    return func(cards)


def add_type(cards: str) -> str:
    if determine_type(cards, five):
        cards = "6" + cards
    elif determine_type(cards, four):
        cards = "5" + cards
    elif determine_type(cards, full_house):
        cards = "4" + cards
    elif determine_type(cards, three):
        cards = "3" + cards
    elif determine_type(cards, two_pair):
        cards = "2" + cards
    elif determine_type(cards, one_pair):
        cards = "1" + cards
    else:
        cards = "0" + cards

    return cards


def p1(f: TextIOWrapper) -> int:
    lines = f.readlines()

    items: list[tuple[str, int]] = []

    for line in lines:
        cards, bit_str = tuple(line.strip().split(" "))
        bit = int(bit_str)
        cards = (
            cards.replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "B")
            .replace("T", "A")
        )

        items.append((add_type(cards), bit))

    items.sort(key=lambda x: x[0])

    res = 0
    for idx, (c, bit) in enumerate(items):
        res += bit * (idx + 1)

    return res


def p2(f: TextIOWrapper) -> int:
    lines = f.readlines()

    items: list[tuple[str, int]] = []

    for line in lines:
        cards, bit_str = tuple(line.strip().split(" "))
        bit = int(bit_str)
        cards = (
            cards.replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "1")
            .replace("T", "A")
        )

        items.append((add_type(cards), bit))

    items.sort(key=lambda x: x[0])

    res = 0
    for idx, (c, bit) in enumerate(items):
        res += bit * (idx + 1)

    return res
