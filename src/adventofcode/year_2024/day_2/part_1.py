from utils import is_safe_report, load_data


def main():
    input_data = load_data()

    safe_reports = sum(is_safe_report(line) for line in input_data)

    print(safe_reports)


if __name__ == "__main__":
    main()
