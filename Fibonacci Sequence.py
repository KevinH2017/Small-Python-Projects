# Fibonacci Sequence

def fib_seq():
    fib_digit = int(input("Enter how many digits to see in the Fibonacci sequence: "))

    num_1 = 0
    num_2 = 1
    num_3 = num_2
    counter = 1

    while counter <= fib_digit:
        print(num_2, end=" ")
        counter += 1
        num_1, num_2 = num_2, num_3
        num_3 = num_1 + num_2
    print("\nFinished Fibonacci Sequence, Closing...")

fib_seq()