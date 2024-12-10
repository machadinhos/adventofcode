from collections.abc import Callable
from multiprocessing import Pool, cpu_count
from pathlib import Path


def load_data() -> list[list[int]]:
    return [list(map(int, line)) for line in Path("input_data.txt").read_text().splitlines()]


def get_all_starting_points(input_data: list[list[int]]) -> list[(int, int)]:
    initial_point = 0
    return [(x, y) for y, line in enumerate(input_data) for x, char in enumerate(line) if char == initial_point]


def solve(input_data: list[list[int]], function: Callable) -> int:
    starting_points = get_all_starting_points(input_data)

    cpus = cpu_count()
    batch_size = max(1, len(starting_points) // cpus)
    starting_points_batches = [starting_points[i : i + batch_size] for i in range(0, len(starting_points), batch_size)]

    batches = [(input_data, spb, 9) for spb in starting_points_batches]
    with Pool(cpus) as p:
        return sum(p.starmap(function, batches))
