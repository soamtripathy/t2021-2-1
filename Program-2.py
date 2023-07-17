def generate_series(x):
    if x <= 0:
        return

    series = []
    number = 1
    step = 2

    while len(series) < x:
        series.append(number)
        number += step
        step += 2

    print("Output:", ", ".join(str(num) for num in series))


def main():
    try:
        x = int(input("Enter a number (x): "))
        generate_series(x)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
