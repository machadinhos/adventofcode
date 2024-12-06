from utils import load_data, calculate_visited


def main():
    input_data = load_data()

    print(calculate_visited(input_data)[0])


if __name__ == "__main__":
    main()
