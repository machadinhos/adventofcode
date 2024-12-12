from pathlib import Path


class Length:
    __slots__ = ["value"]

    def __init__(self, value: int = 0):
        self.value = value


class Node:
    __slots__ = ("length", "next", "value")

    def __init__(self, value: str, length: Length, next_node: "Node" = None) -> None:
        self.value = value
        self.next = next_node
        length.value = length.value + 1
        self.length = length

    def __len__(self):
        return self.length.value


def get_node(input_data: list[str]) -> Node:
    head = Node(input_data[-1], length=Length())
    for value in reversed(input_data[:-1]):
        head = Node(value, head.length, head)

    return head


def load_data() -> list[str]:
    return Path("input_data.txt").read_text().split()


def get_next_str(num: str) -> list[str]:
    if num == "0":
        num = ["1"]
    elif (length := len(num)) % 2 == 0:
        num = (str(int(num[: length // 2])), str(int(num[length // 2 :])))
    else:
        num = [str(int(num) * 2024)]
    return num
