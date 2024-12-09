import json
from pathlib import Path


def load_data() -> (list[int], list[int]):
    with Path("input_data.json").open("r") as f:
        input_data: list[int] = json.load(f)

    left, right = [], []

    for index, value in enumerate(input_data):
        left.append(value) if index % 2 == 0 else right.append(value)

    return left, right
