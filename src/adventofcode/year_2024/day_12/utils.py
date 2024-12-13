from pathlib import Path


def load_data() -> list[str]:
    return Path("input_data.txt").read_text().splitlines()




def get_neighbors(x, y, grid):
    neighbors = []
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors


def flood_fill(x, y, grid, visited):
    value = grid[y][x]
    stack = [(x, y)]
    group = []

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            group.append((cx, cy))

            for nx, ny in get_neighbors(cx, cy, grid):
                if grid[ny][nx] == value and (nx, ny) not in visited:
                    stack.append((nx, ny))

    return group


def find_groups(grid):
    visited = set()
    groups = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) not in visited:
                groups.append(flood_fill(x, y, grid, visited))

    return groups
