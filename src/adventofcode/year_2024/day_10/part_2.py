from utils import load_data, solve


def get_num_distinct_paths(input_data: list[list[int]], starting_points, end_char: int) -> int:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    height, width = len(input_data), len(input_data[0])

    def dfs(x: int, y: int, current_value: int):
        if current_value == end_char:
            return 1

        path_count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height and input_data[ny][nx] == current_value + 1:
                path_count += dfs(nx, ny, current_value + 1)

        return path_count

    total_paths = 0

    for i, j in starting_points:
        total_paths += dfs(i, j, 0)

    return total_paths


def main():
    input_data = load_data()

    print(solve(input_data, get_num_distinct_paths))


if __name__ == "__main__":
    main()
