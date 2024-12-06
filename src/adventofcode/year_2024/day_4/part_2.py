from typing import Literal
from utils import load_data
import re


def is_possible(
    x: int,
    y: int,
    searchable: list[str],
    substring: str,
    x_offset: Literal[1, -1],
    y_offset: Literal[1, -1],
) -> bool:
    if searchable[y + y_offset][x + x_offset] == substring[0]:
        return searchable[y - y_offset][x - x_offset] == substring[-1]
    elif searchable[y + y_offset][x + x_offset] == substring[-1]:
        return searchable[y - y_offset][x - x_offset] == substring[0]
    else:
        return False


def search_x(x: int, y: int, searchable: list[str], substring: str) -> bool:
    return is_possible(x, y, searchable, substring, -1, -1) and is_possible(
        x, y, searchable, substring, -1, 1
    )


def main():
    input_data = load_data()

    mas = "MAS"

    x_mas_count = 0
    for y in range(1, len(input_data) - 1):
        for x in (
            match.start() + 1 for match in re.finditer(mas[1], input_data[y][1:-1])
        ):
            if search_x(x, y, input_data, mas):
                x_mas_count += 1

    print(x_mas_count)


if __name__ == "__main__":
    main()
