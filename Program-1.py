class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b


def main():
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        operation = input("Enter the type of operation (+, -, *, /): ")

        calculator = Calculator(a, b)

        if operation == '+':
            result = calculator.add()
        elif operation == '-':
            result = calculator.subtract()
        elif operation == '*':
            result = calculator.multiply()
        elif operation == '/':
            result = calculator.divide()
        else:
            print("Invalid operation entered.")
            return

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
