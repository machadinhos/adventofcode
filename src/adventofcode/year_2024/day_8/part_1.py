from utils import load_data, get_towers_coords, towers_coords_loop


def main():
    input_data = load_data()

    height = len(input_data)
    width = len(input_data[0])

    towers = get_towers_coords(input_data)

    unique_locations = set()
    for (x1, y1), (x2, y2) in towers_coords_loop(towers):
        vx, vy = x2 - x1, y2 - y1
        if 0 <= (new_x := x1 - vx) < width and 0 <= (new_y := y1 - vy) < height:
            unique_locations.add((new_x, new_y))
        if 0 <= (new_x := x2 + vx) < width and 0 <= (new_y := y2 + vy) < height:
            unique_locations.add((new_x, new_y))

    print(len(unique_locations))


if __name__ == "__main__":
    main()
