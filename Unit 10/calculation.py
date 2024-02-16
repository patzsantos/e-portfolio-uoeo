def add(x, y):  # adding two numbers
    return x + y


def subtract(x, y):  # subtracting two numbers
    return x - y


def multiply(x, y):  # multiplying two numbers
    return x * y


def divide(x, y):  # dividing two numbers
    return x / y


# display selection of operation choices
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# program loop
while True:
    choice = input("Enter choice (1,2,3,4): ")

# if the choice is valid
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # execute the operation selected by the user
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

        # ask the user if he/she wants to do another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")

        # end the loop if user does not want to do another calculation
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid Input")  # display invalid message
