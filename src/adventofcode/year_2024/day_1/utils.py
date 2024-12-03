import json
from pathlib import Path


def load_data() -> (list[int], list[int]):
    input_data: list[int] = json.load(Path("input_data.json").open("r"))

    left, right = [], []

    for index, value in enumerate(input_data):
        left.append(value) if index % 2 == 0 else right.append(value)

    return left, right
