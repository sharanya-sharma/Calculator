def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
