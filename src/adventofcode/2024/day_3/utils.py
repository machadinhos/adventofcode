import re
from collections.abc import Generator
from pathlib import Path


def load_data() -> str:
    return Path("input_data.txt").read_text()


def get_number_sequences(data) -> Generator[tuple[int, int], None, None]:
    valid_regex = r"mul\(\d+,\d+\)"
    number_sequences = (
        match.group()[4:-1].split(",") for match in re.finditer(valid_regex, data)
    )
    return ((int(x), int(y)) for x, y in number_sequences)


def mult_all(sequence: Generator[tuple[int, int], None, None]) -> Generator[int]:
    return (x * y for x, y in sequence)
