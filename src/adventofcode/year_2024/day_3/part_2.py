from utils import get_number_sequences, load_data, mult_all


def main():
    input_data = load_data()

    split_dont_data = input_data.split("don't()")

    enabled_part = "".join(
        (
            split_dont_data[0],
            *(dont_portion[dont_portion.find("do()") :] for dont_portion in split_dont_data),
        )
    )

    result = sum(mult_all(get_number_sequences(enabled_part)))

    print(result)


if __name__ == "__main__":
    main()
