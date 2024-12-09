from operator import add, mul

from utils import calculate_result, load_data


def concat(x, y):
    return int(str(x) + str(y))


def main():
    input_data = load_data()

    possible_operations = (mul, add, concat)

    result = calculate_result(input_data, possible_operations, True)

    print(result)


if __name__ == "__main__":
    main()
