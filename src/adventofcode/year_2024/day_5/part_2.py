from utils import load_data


def is_ordered(page: list[str], rules: dict[str : list[str]]) -> (bool, int):
    cant_appear = set()
    for index, item_num in enumerate(page):
        if item_num in cant_appear:
            break
        cant_appear.update(rules[item_num])
    else:
        return True, None
    return False, index


def reorder_list(
    page: list[str], rules: dict[str : list[str]], prob_index: int
) -> list[str]:
    page[prob_index], page[prob_index - 1] = page[prob_index - 1], page[prob_index]
    ordered, prob_index = is_ordered(page, rules)
    while not ordered:
        page[prob_index], page[prob_index - 1] = page[prob_index - 1], page[prob_index]
        ordered, prob_index = is_ordered(page, rules)
    return page


def main():
    rules, pages = load_data()

    result = 0
    for page in pages:
        ordered, prob_index = is_ordered(list(reversed(page)), rules)
        if not ordered:
            new_list = reorder_list(list(page), rules, prob_index)
            result += int(new_list[len(new_list) // 2])

    print(result)


if __name__ == "__main__":
    main()
