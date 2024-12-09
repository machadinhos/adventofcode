from itertools import cycle
from pathlib import Path


def load_data() -> list[str]:
    return Path("input_data.txt").read_text().splitlines()


def find_initial_guard_position(input_data: list[str]) -> (int, int):
    guard = "^"
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char == guard:
                return x, y

    raise Exception("No initial guard found")


def calculate_visited(input_data: list[str], initial_pos: (int, int) = None) -> (int | None, set[(int, int)]):
    if initial_pos is None:
        x, y = find_initial_guard_position(input_data)
    else:
        x, y = initial_pos

    width = len(input_data[0])
    height = len(input_data)

    directions = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))
    direction_move: (int, int) = next(directions)

    distinct_positions = {(x, y)}
    positions_after_obstacle = set()
    while 0 <= (new_x := x + direction_move[0]) < width and 0 <= (new_y := y + direction_move[1]) < height:
        if input_data[new_y][new_x] == "#":
            while input_data[new_y][new_x] == "#":
                direction_move = next(directions)
                new_x = x + direction_move[0]
                new_y = y + direction_move[1]
            pos = (x, y, new_x, new_y)
            if pos in positions_after_obstacle:
                return None, distinct_positions
            positions_after_obstacle.add(pos)
        x = new_x
        y = new_y
        distinct_positions.add((x, y))

    return len(distinct_positions), distinct_positions


def print_guard_movement(
    input_data: list[str],
    guard_pos: set[(int, int)],
    highlighted_pos: (int, int) = None,
) -> None:
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if (x, y) == highlighted_pos or char == "^":
                print(f"\033[31m{char}\033[0m", end="")
            elif (x, y) in guard_pos:
                print("+", end="")
            else:
                print(char, end="")
        print()
