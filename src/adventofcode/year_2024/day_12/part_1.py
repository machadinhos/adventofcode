from utils import find_groups, load_data


def main():
    input_data = load_data()

    groups = find_groups(input_data)

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    result = 0
    for group in groups:
        area = len(group)
        perimeter = 0
        for x, y in group:
            for dx, dy in directions:
                if (x + dx, y + dy) not in group:
                    perimeter += 1
        result += area * perimeter

    print(result)


if __name__ == "__main__":
    main()
