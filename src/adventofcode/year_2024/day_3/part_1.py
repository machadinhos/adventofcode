from utils import load_data, get_number_sequences, mult_all

def main():
    input_data = load_data()

    result = sum(mult_all(get_number_sequences(input_data)))

    print(result)

if __name__ == "__main__":
    main()
