from utils import Node, get_node, load_data


def get_next_iteration(head: Node) -> Node:
    current = head

    while current is not None:
        if current.value == "0":
            current.value = "1"
        elif (length := len(current.value)) % 2 == 0:
            value = current.value
            current.value = value[: length // 2]
            current.next = Node(str(int(value[length // 2 :])), current.length, current.next)
            current = current.next
        else:
            current.value = str(int(current.value) * 2024)
        current = current.next

    return head


def main():
    input_data = get_node(load_data())

    for _ in range(25):
        input_data = get_next_iteration(input_data)

    print(len(input_data))


if __name__ == "__main__":
    main()
