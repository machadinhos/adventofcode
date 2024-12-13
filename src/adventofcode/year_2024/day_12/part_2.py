from utils import find_groups, load_data


def count_edges(x: int, y: int, group: list[(int, int)]) -> int:
    right = lambda cx, cy: (cx + 1, cy)
    left = lambda cx, cy: (cx - 1, cy)
    up = lambda cx, cy: (cx, cy - 1)
    down = lambda cx, cy: (cx, cy + 1)

    edges = 0

    not_has_up = up(x, y) not in group
    not_has_down = down(x, y) not in group
    not_has_left = left(x, y) not in group
    not_has_right = right(x, y) not in group

    if not_has_right:
        if not_has_down:
            edges += 1
        if not_has_up:
            edges += 1
    if not_has_left:
        if not_has_down:
            edges += 1
        if not_has_up:
            edges += 1

    not_has_up_left = up(*left(x, y)) not in group
    not_has_down_left = down(*left(x, y)) not in group
    not_has_up_right = up(*right(x, y)) not in group
    not_has_down_right = down(*right(x, y)) not in group

    if not_has_up_left and not not_has_up and not not_has_left:
        edges += 1
    if not_has_down_left and not not_has_down and not not_has_left:
        edges += 1
    if not_has_up_right and not not_has_up and not not_has_right:
        edges += 1
    if not_has_down_right and not not_has_down and not not_has_right:
        edges += 1

    return edges


def main():
    input_data = load_data()

    groups = find_groups(input_data)

    result = 0
    for group in groups:
        area = len(group)
        sides = 0
        for x, y in group:
            sides += count_edges(x, y, group)
        result += area * sides

    print(result)


if __name__ == "__main__":
    main()
