from pathlib import Path

from utils import load_data


def main():
    input_data = load_data()

    lengths = {}
    result = 0
    for index, x in enumerate(input_data):
        print(f"{index + 1} of {len(input_data)}")
        nums_of_x = Path(f"helper/nums_after_37/{x}.txt").read_text().split()
        for y in nums_of_x:
            if y not in lengths:
                nums_of_y = Path(f"helper/nums_after_37/{y}.txt").read_text().split()
                y_length = len(nums_of_y)
                for z in nums_of_y:
                    if len(z) % 2 == 0:
                        y_length += 1
                lengths[y] = y_length
            result += lengths[y]

    print(result)


if __name__ == "__main__":
    main()
