from collections.abc import Callable
from itertools import product
from typing import Iterator, Tuple
from pathlib import Path
from multiprocessing import Pool


def load_data() -> list[(int, list[int])]:
    lines = Path("input_data.txt").read_text().splitlines()

    data = [
        (int(left), tuple(map(int, right.split())))
        for item in lines
        for left, right in [item.split(": ")]
    ]

    return data


def generate_combinations[T](
    length: int, values: tuple[T, ...]
) -> Iterator[Tuple[T, ...]]:
    return product(values, repeat=length)


def process_input_data(
    data: tuple[int, list[int]], possible_operations: tuple[Callable, ...]
) -> int:
    result, nums = data
    for operation_group in generate_combinations(len(nums) - 1, possible_operations):
        current_value = nums[0]
        for operation, num in zip(operation_group, nums[1:]):
            current_value = operation(current_value, num)
        if current_value == result:
            return result
    return 0


def calculate_result(
    input_data: list[tuple[int, list[int]]],
    possible_operations: tuple[Callable, ...],
    multi_process: bool = False,
) -> int:
    if multi_process:
        with Pool() as pool:
            results = pool.starmap(
                process_input_data, [(data, possible_operations) for data in input_data]
            )
    else:
        results = [process_input_data(data, possible_operations) for data in input_data]

    return sum(results)
