from utils import get_number_sequences, load_data, mult_all


def main():
    input_data = load_data()

    result = sum(mult_all(get_number_sequences(input_data)))

    print(result)


if __name__ == "__main__":
    main()
