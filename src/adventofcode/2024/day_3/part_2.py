from utils import load_data, get_number_sequences, mult_all

if __name__ == "__main__":
    input_data = load_data()

    split_dont_data = input_data.split("don't()")

    enabled_part = "".join(
        (
            split_dont_data[0],
            *(
                dont_portion[dont_portion.find("do()") :]
                for dont_portion in split_dont_data
            ),
        )
    )

    result = sum(mult_all(get_number_sequences(enabled_part)))

    print(result)
