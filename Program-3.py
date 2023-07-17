def generate_series(x):
    if x <= 0:
        return

    series = []
    number = 1

    while number <= x:
        series.append(number)
        number += 2

    print("Output:", ", ".join(str(num) for num in series))


def main():
    try:
        x = int(input("Enter a number (x): "))
        generate_series(x)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
