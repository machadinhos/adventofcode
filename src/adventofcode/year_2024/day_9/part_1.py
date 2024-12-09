from utils import load_data


def main():
    input_data: list[str] = load_data()

    index_left = 0
    for index_right in range(len(input_data) - 1, -1, -1):
        if input_data[index_right] == ".":
            continue
        while input_data[index_left] != ".":
            index_left += 1
        if index_left > index_right:
            break
        input_data[index_left], input_data[index_right] = (
            input_data[index_right],
            input_data[index_left],
        )

    result = 0
    for index, char in enumerate(input_data[1 : input_data.index(".")], 1):
        result += int(char) * index

    print(result)


if __name__ == "__main__":
    main()
