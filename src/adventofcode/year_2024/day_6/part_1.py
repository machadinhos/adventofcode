from utils import calculate_visited, load_data


def main():
    input_data = load_data()

    print(calculate_visited(input_data)[0])


if __name__ == "__main__":
    main()
