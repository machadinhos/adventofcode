from pathlib import Path


def load_data() -> list[str]:
    return Path("input_data.txt").read_text().splitlines()


def print_found(lines: list[str], found_coords: set[(int, int)]):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (x, y) in found_coords:
                print(f"\033[31m{char}\033[0m", end="")
            else:
                print(char, end="")
        print()
