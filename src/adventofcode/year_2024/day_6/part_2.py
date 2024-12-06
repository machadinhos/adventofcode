from multiprocessing import Pool, cpu_count
from utils import (
    load_data,
    calculate_visited,
    find_initial_guard_position,
)


def process_guard_position(args: (int, int, list[str], (int, int))) -> bool:
    x, y, input_data, initial_position = args

    modified_data = input_data.copy()
    modified_data[y] = modified_data[y][:x] + "#" + modified_data[y][x + 1 :]

    return calculate_visited(modified_data, initial_position)[0] is None


def main():
    input_data = load_data()

    initial_position = find_initial_guard_position(input_data)
    all_guard_positions = calculate_visited(input_data, initial_position)[1]

    args = [
        (x, y, input_data, initial_position)
        for x, y in all_guard_positions
        if (x, y) != initial_position
    ]

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_guard_position, args)

    print(sum(results))


if __name__ == "__main__":
    main()
