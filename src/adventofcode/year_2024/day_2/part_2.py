from utils import is_safe_report, load_data


def main():
    input_data = load_data()

    safe_reports = sum(any(is_safe_report(line[:i] + line[i + 1 :]) for i in range(len(line))) for line in input_data)

    print(safe_reports)


if __name__ == "__main__":
    main()
