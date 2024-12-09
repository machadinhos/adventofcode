from pathlib import Path


def load_data() -> list[str]:
    text = Path("input_data.txt").read_text()

    result = []
    is_storage = True
    index = 0
    for char in text:
        if is_storage:
            result.extend([str(index)] * int(char))
            index += 1
        else:
            result.extend(["."] * int(char))
        is_storage = not is_storage

    return result
