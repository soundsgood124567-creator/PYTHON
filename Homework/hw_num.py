
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))


match choice:
    case 1:
        print("Result =", num1 + num2)

    case 2:
        print("Result =", num1 - num2)

    case 3:
        print("Result =", num1 * num2)

    case 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error")

    case 5:
        print("Exited")

