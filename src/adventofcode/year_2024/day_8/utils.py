from collections import defaultdict
from itertools import combinations
from pathlib import Path


def load_data() -> list[str]:
    return Path("input_data.txt").read_text().splitlines()


def get_towers_coords(input_data: list[str]) -> dict[str, list[(int, int)]]:
    towers = defaultdict(list)

    for index_y, y in enumerate(input_data):
        for index_x, x in enumerate(y):
            if x == ".":
                continue
            towers[x].append((index_x, index_y))

    return towers


def towers_coords_loop(
    towers_coords: dict[str, list[(int, int)]],
) -> ((int, int), (int, int)):
    for locations in towers_coords.values():
        tower_combos = combinations(locations, 2)
        for (x1, y1), (x2, y2) in tower_combos:
            yield (x1, y1), (x2, y2)
