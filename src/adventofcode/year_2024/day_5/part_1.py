from utils import load_data

def main():
    rules, pages = load_data()

    result = 0
    for page in pages:
        cant_appear = set()
        for item in reversed(page):
            if item in cant_appear:
                break
            cant_appear.update(rules[item])
        else:
            result += int(page[len(page) // 2])

    print(result)

if __name__ == '__main__':
    main()
