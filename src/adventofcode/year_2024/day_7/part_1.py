from utils import load_data, calculate_result
from operator import mul, add

def main():
    input_data = load_data()

    possible_operations = (mul, add)

    result = calculate_result(input_data, possible_operations)

    print(result)


if __name__ == '__main__':
    main()