# 5 programs that uses loops and functions

def fibonacci(n):  # [1] Finding the mth Fibonacci number including the 0 (functions and loops)
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a
            a = b
            b = c + a
        return b


def calculate_bmi(weight, height):  # [2] BMI Calculator (function)
    bmi = weight / (height ** 2)
    return bmi


def check_bmi_category(bmi):  # [2] BMI Indicator (function)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def square(x):  # [3] Finding the square (function)
    return x * x


# [4] Operations for the basic calculator (function)
def add(x, y):
    return x + y


def difference(x, y):
    return x - y


def product(x, y):
    return x * y


def division(x, y):
    return x / y


def is_leap_year(year):  # [5] Leap year checker (function)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# Menu structure
while True:
    print("Choose a program to run:")
    print("[1] Find the nth Fibonacci number")
    print("[2] Calculate your BMI")
    print("[3] Finding the square of a number")
    print("[4] Basic calculator")
    print("[5] Leap year checker")
    choice = input("Type in the number on what program you want to run: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if choice == 1:
        while True:
            try:
                number = int(input("Enter a number to find its fibonacci value: "))
                print("Fibonacci value of", number, "is", fibonacci(number))
                break
            except ValueError:  # Except is used so that users are encouraged to use an appropriate value to type.
                print("Invalid input. Please enter a valid number.")
    elif choice == 2:
        while True:  # Choice [2] call the function, while loop is implemented.
            try:
                weight = float(input("Enter your weight in kg: "))
                height = float(input("Enter your height in meters: "))
                bmi = calculate_bmi(weight, height)
                print("Your BMI is:", bmi)
                bmi_category = check_bmi_category(bmi)
                print("You are:", bmi_category)
            except ValueError:  # try-except statements are used so that users are encouraged to use an appropriate value to type
                print("Invalid input. Please enter a valid number.")
                continue
            choice = input("Do you want to calculate again? Type Yes or No:")
            if choice.lower() == "yes":
                continue
            elif choice.lower() == "no":
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'")
    elif choice == 3:
        while True:  # Choice [3] call the function square(x), the while loop is implemented here.
            n = input("Enter a number (Please type 'Quit' to quit): ")
            try:
                n = int(n)
                print(square(n))
            except ValueError:  # Except is used to prevent the ValueError error wherein if the user tries to input
                # an inappropriate value, it will bypass the if statement, and will print what is under the else
                # statement.
                if n == 'Quit':
                    break
                else:
                    print("Invalid Input. Try Again.")
    elif choice == 4:
        while True:  # Choice [4] call the basic mathematical operations functions, and the while loop is implemented.
            print("Basic Calculator:")
            print("1. Sum (Add)")
            print("2. Difference (Subtract)")
            print("3. Product (Multiply)")
            print("4. Quotient (Divide)")
            print("5. Quit")
            try:
                choice = int(input("Choose an operation: "))
                if choice == 1:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    print("Sum:", add(x, y))
                elif choice == 2:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    print("Difference:", difference(x, y))
                elif choice == 3:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    print("Product:", product(x, y))
                elif choice == 4:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    print("Quotient:", division(x, y))
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:  # try-except statements are used so that users are encouraged to use an appropriate value to type
                print("Invalid input. Please enter a valid number.")
    elif choice == 5:
        while True:  # Choice [5] call the function, while and for loop is implemented for this program.
            try:
                year = int(input("Please enter the year you would like to start checking leap years from: "))
                total_years = int(input("Please enter over how many years you would like to check: "))
                if year <= 0:
                    print("Year should be greater than 0")
                else:
                    for a in range(year, year + total_years):
                        if is_leap_year(a):
                            print(f"{a} is a leap year")
                        else:
                            print(f"{a} is not a leap year")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid year.")
    else:
        print("Invalid choice. Try again")