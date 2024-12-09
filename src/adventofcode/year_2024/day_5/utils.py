from collections import defaultdict
from pathlib import Path


def load_data() -> (defaultdict[str : list[str]], list[list[str]]):
    rules, pages = Path("input_data.txt").read_text().split("\n\n")

    rules_dict = defaultdict(set)
    for pair in rules.splitlines():
        key, value = pair.split("|")
        rules_dict[key].add(value)

    return rules_dict, [line.split(",") for line in pages.splitlines()]
