from utils import load_data, is_safe_report

if __name__ == "__main__":
    input_data = load_data()

    safe_reports = sum(is_safe_report(line) for line in input_data)

    print(safe_reports)
