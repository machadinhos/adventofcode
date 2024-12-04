from typing import Literal
from utils import load_data
import re


def is_possible(
    x_coord: int,
    y_coord: int,
    searchable: list[str],
    substring: str,
    x_offset: Literal[1, -1],
    y_offset: Literal[1, -1],
) -> bool:
    if searchable[y_coord + y_offset][x_coord + x_offset] == substring[0]:
        return searchable[y_coord - y_offset][x_coord - x_offset] == substring[-1]
    elif searchable[y_coord + y_offset][x_coord + x_offset] == substring[-1]:
        return searchable[y_coord - y_offset][x_coord - x_offset] == substring[0]
    else:
        return False


def search_x(
    x_coord: int, y_coord: int, searchable: list[str], substring: str
) -> bool:
    return is_possible(x_coord, y_coord, searchable, substring, -1, -1) and is_possible(
        x_coord, y_coord, searchable, substring, -1, 1
    )


if __name__ == "__main__":
    input_data = load_data()

    MAS = "MAS"

    x_mas_count = 0
    for y in range(1, len(input_data) - 1):
        for x in (
            match.start() + 1 for match in re.finditer(MAS[1], input_data[y][1:-1])
        ):
            if search_x(x, y, input_data, MAS):
                x_mas_count += 1

    print(x_mas_count)
