from utils import load_data, calculate_result
from operator import mul, add

def concat(x, y):
    return int(str(x) + str(y))

def main():
    input_data = load_data()

    possible_operations = (mul, add, concat)

    result = calculate_result(input_data, possible_operations, True)

    print(result)


if __name__ == '__main__':
    main()