from utils import load_data, solve


def get_distinct_scores(input_data: list[list[int]], starting_points, end_char: int) -> set[int, int]:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    height, width = len(input_data), len(input_data[0])

    def dfs(x: int, y: int, current_value: int, visited_ends) -> set[int, int]:
        if current_value == end_char:
            visited_ends.add((x, y))
            return visited_ends

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height and input_data[ny][nx] == current_value + 1:
                dfs(nx, ny, current_value + 1, visited_ends)

        return visited_ends

    score = 0
    for i, j in starting_points:
        score += len(dfs(i, j, 0, set()))

    return score


def main():
    input_data = load_data()

    print(solve(input_data, get_distinct_scores))


if __name__ == "__main__":
    main()
