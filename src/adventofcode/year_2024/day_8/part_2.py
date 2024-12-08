from adventofcode.year_2024.day_8.utils import get_towers_coords, towers_coords_loop
from utils import load_data


def main():
    input_data = load_data()

    height = len(input_data)
    width = len(input_data[0])

    towers = get_towers_coords(input_data)

    unique_locations = {
        coords
        for coords_list in towers.values()
        for coords in coords_list
        if len(coords_list) > 1
    }
    for (x1, y1), (x2, y2) in towers_coords_loop(towers):
        vx, vy = x2 - x1, y2 - y1
        new_x, new_y = x1, y1
        while (
            0 <= (new_x := new_x - vx) < width and 0 <= (new_y := new_y - vy) < height
        ):
            unique_locations.add((new_x, new_y))
        new_x, new_y = x2, y2
        while (
            0 <= (new_x := new_x + vx) < width and 0 <= (new_y := new_y + vy) < height
        ):
            unique_locations.add((new_x, new_y))

    print(len(unique_locations))


if __name__ == "__main__":
    main()
