from pathlib import Path
from collections import defaultdict


def load_data() -> (defaultdict[str: list[str]], list[list[str]]):
    rules, pages = Path("input_data.txt").read_text().split('\n\n')

    rules_dict = defaultdict(set)
    for pair in rules.splitlines():
        key, value = pair.split("|")
        rules_dict[key].add(value)

    pages = [
        [num for num in line.split(",")]
        for line in pages.splitlines()
    ]

    return rules_dict, pages
