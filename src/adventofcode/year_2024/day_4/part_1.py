from enum import Enum
from utils import load_data
import re


class Direction(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    DIAG_RIGHT_UP = (-1, -1)
    DIAG_RIGHT_DOWN = (1, 1)
    DIAG_LEFT_UP = (1, -1)
    DIAG_LEFT_DOWN = (-1, 1)

    def move(self, x_coord: int, y_coord: int) -> (int, int):
        dx, dy = self.value
        return x_coord + dx, y_coord + dy

    def can_search(
        self,
        x_coord: int,
        y_coord: int,
        search_len: int,
        line_len: int,
        col_height: int,
    ) -> bool:
        dx, dy = self.value
        target_x = x_coord + dx * (search_len - 1)
        target_y = y_coord + dy * (search_len - 1)
        return 0 <= target_x <= line_len - 1 and 0 <= target_y <= col_height - 1


def search_direction(
    x_coord: int,
    y_coord: int,
    direction_movement: Direction,
    searchable: list[str],
    substring: str,
) -> bool:
    matches = 1
    while matches < len(substring):
        x_coord, y_coord = direction_movement.move(x_coord, y_coord)
        if searchable[y_coord][x_coord] != substring[matches]:
            return False
        matches += 1
    return True


if __name__ == "__main__":
    input_data = load_data()

    XMAS = "XMAS"
    XMAS_LEN = len(XMAS)
    COL_HEIGHT = len(input_data)
    LINE_LEN = len(input_data[0])

    xmas_count = 0
    for y in range(COL_HEIGHT):
        for x in (match.start() for match in re.finditer(XMAS[0], input_data[y])):
            for direction in Direction:
                if direction.can_search(
                    x, y, XMAS_LEN, LINE_LEN, COL_HEIGHT
                ) and search_direction(x, y, direction, input_data, XMAS):
                    xmas_count += 1

    print(xmas_count)
