from operator import add, mul

from utils import calculate_result, load_data


def main():
    input_data = load_data()

    possible_operations = (mul, add)

    result = calculate_result(input_data, possible_operations)

    print(result)


if __name__ == "__main__":
    main()
