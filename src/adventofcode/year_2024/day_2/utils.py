import json
from pathlib import Path


def load_data() -> list[list[int]]:
    with Path("input_data.json").open("r") as f:
        return json.load(f)


def is_safe_report(report: list[int]) -> bool:
    prev = report[0]
    order = "d" if prev > report[1] else "a"
    for i in report[1:]:
        if (order == "d" and prev <= i) or (order == "a" and prev >= i) or abs(i - prev) > 3:
            break
        prev = i
    else:
        return True
    return False
