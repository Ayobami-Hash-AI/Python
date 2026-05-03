print("Hello and welcome to this simple calculator")

while True:
    print("\nPlease choose the operation which you want to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit Calculator")

    try:
        choice = int(input("Enter the choice which you want to perform: "))

        if choice == 5:
            print("Calculator closed.")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select between 1 and 5.")
            continue

        a = float(input("Enter the Value of A: "))
        b = float(input("Enter the Value of B: "))

        if choice == 1:
            result = a + b
            print("The result is:", result)

        elif choice == 2:
            result = a - b
            print("The result is:", result)

        elif choice == 3:
            result = a * b
            print("The result is:", result)

        elif choice == 4:
            result = a / b
            print("The result is:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

    finally:
        print("Operation completed.")