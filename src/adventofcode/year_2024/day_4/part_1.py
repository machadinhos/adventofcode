import re
from enum import Enum

from utils import load_data


class Direction(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    DIAG_RIGHT_UP = (-1, -1)
    DIAG_RIGHT_DOWN = (1, 1)
    DIAG_LEFT_UP = (1, -1)
    DIAG_LEFT_DOWN = (-1, 1)

    def move(self, x: int, y: int) -> (int, int):
        dx, dy = self.value
        return x + dx, y + dy

    def can_search(
        self,
        x: int,
        y: int,
        search_len: int,
        line_len: int,
        col_height: int,
    ) -> bool:
        dx, dy = self.value
        target_x = x + dx * (search_len - 1)
        target_y = y + dy * (search_len - 1)
        return 0 <= target_x <= line_len - 1 and 0 <= target_y <= col_height - 1


def search_direction(
    x: int,
    y: int,
    direction: Direction,
    searchable: list[str],
    substring: str,
) -> bool:
    matches = 1
    while matches < len(substring):
        x, y = direction.move(x, y)
        if searchable[y][x] != substring[matches]:
            return False
        matches += 1
    return True


def main():
    input_data = load_data()

    xmas = "XMAS"
    xmas_len = len(xmas)
    col_height = len(input_data)
    line_len = len(input_data[0])

    xmas_count = 0
    for y in range(col_height):
        for x in (match.start() for match in re.finditer(xmas[0], input_data[y])):
            for direction in Direction:
                if direction.can_search(x, y, xmas_len, line_len, col_height) and search_direction(
                    x, y, direction, input_data, xmas
                ):
                    xmas_count += 1

    print(xmas_count)


if __name__ == "__main__":
    main()
