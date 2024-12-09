from utils import load_data


def get_dot_len_index(input_data: list[str]) -> list[(int, int)]:
    dots = []
    current_dot_start_index = input_data.index(".")
    i = current_dot_start_index
    while i < len(input_data):
        if input_data[i] != ".":
            dots.append((i - current_dot_start_index, current_dot_start_index))
            while i < len(input_data) and input_data[i] != ".":
                i += 1
            current_dot_start_index = i
        i += 1
    return sorted(dots, key=lambda x: x[1])


def get_viable_dots(dots: list[(int, int)], required_len: int) -> (int, int):
    for dots_list_index, (length, index) in enumerate(dots):
        if length >= required_len:
            return index, dots_list_index
    return None


def nums_sequence(input_data: list[str]) -> (int, int):
    index_end = len(input_data)
    i = index_end - 1
    current_file = input_data[i]
    while i > 0:
        if input_data[i] != current_file:
            yield i + 1, index_end
            while i > 0 and input_data[i] == ".":
                i -= 1
            index_end = i + 1
            current_file = input_data[i]
        i -= 1
    return None


def main():
    input_data = load_data()

    dots = get_dot_len_index(input_data)

    for start, end in nums_sequence(input_data):
        file_len = end - start
        dots_location = get_viable_dots(dots, file_len)
        if dots_location is not None:
            data_index, dots_list_index = dots_location
            if data_index > start:
                continue
            input_data[start:end], input_data[data_index : data_index + file_len] = (
                input_data[data_index : data_index + file_len],
                input_data[start:end],
            )
            dots[dots_list_index] = (dots[dots_list_index][0] - file_len, data_index + file_len)

    result = 0
    for index, file in enumerate(input_data):
        if file == ".":
            continue
        result += int(file) * index

    print(result)


if __name__ == "__main__":
    main()
    a = [1, 2]
