# Collatz Conjecture

# if num is even, divide by 2               num / 2
# if num is odd, times by 3 and add 1       3 * num + 1
# eventually any integer will equal 1
def collatz(num):
    count = 0
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
            count += 1
        else:
            num = int(3 * num + 1)
            count += 1
    else:
        print(num)
        print("Finished!")
        print("It took", count, "steps to reach 1.")

# Takes user input and checks if input is positive integer
def input_value():
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num < 0:
                print("Input must be a positive integer! ")
                continue
            break
        except ValueError:
            print("ERROR, INPUT INTEGERS ONLY")
    # Runs collatz algorithm
    collatz(num)

input_value()