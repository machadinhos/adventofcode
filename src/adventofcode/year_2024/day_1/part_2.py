from utils import load_data


def main():
    left, right = load_data()
    amount = 0

    for value in left:
        amount += value * right.count(value)

    print(amount)


if __name__ == "__main__":
    main()
