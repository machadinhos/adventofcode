from utils import load_data


def main():
    left, right = load_data()

    left = sorted(left)
    right = sorted(right)

    absolute = 0

    for i, j in zip(left, right):
        absolute += abs(i - j)

    print(absolute)


if __name__ == "__main__":
    main()
