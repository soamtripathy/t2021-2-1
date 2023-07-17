def count_multiples(numbers_list):
    multiples_count = {num: 0 for num in range(1, 10)}

    for number in numbers_list:
        for i in range(1, 10):
            if number % i == 0:
                multiples_count[i] += 1

    return multiples_count


def main():
    try:
        input_list = [int(num) for num in input("Enter the list of numbers separated by spaces: ").split()]
        result = count_multiples(input_list)
        print("Output:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
