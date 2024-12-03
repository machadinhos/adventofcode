from utils import load_data

if __name__ == "__main__":
    left, right = load_data()
    amount = 0

    for value in left:
        amount += value * right.count(value)

    print(amount)
