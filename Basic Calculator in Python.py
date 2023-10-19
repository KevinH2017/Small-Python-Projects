# Calculator in Python

# Functions for math operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Displays options for operations
print("Python Calculator, Select an Operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

while True:
    # User chooses operation
    user_input = input("Enter Number for Operation (1, 2, 3, 4): ")

    # Keeps asking for valid user input of "1", "2", "3", or "4"
    if user_input not in ("1", "2", "3", "4"):
        print("ERROR, PLEASE INPUT 1, 2, 3, OR 4")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
    else:
        # float allows for decimal input
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))

        # Calculations for first and second numbers user inputted
        if user_input == "1":
            print(num_1, " + ", num_2, " = ", add(num_1, num_2))
        elif user_input == "2":
            print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
        elif user_input == "3":
            print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
        elif user_input == "4":
            print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
            
        # Asks user if they want to continue using the calculator, otherwise it will break
        next_calc = input("Do you want to do another calculation? (y / n): ").lower()
        if next_calc not in ("y", "n"):
            next_calc = input("ERROR, PLEASE INPUT y OR n").lower()
        elif next_calc == "y":
            continue            # Restarts calculator
        elif next_calc == "n":
            print("Exiting Program...")
            break               # Exits calculator