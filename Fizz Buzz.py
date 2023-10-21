# Fizz Buzz

# For 1 to n, multiples of three print "Fizz", 
# multiples of five print "Buzz", 
# multiples of three and five print "FizzBuzz"
def fizz_buzz(n):
    # Starts at 1 and ends at n
    for i in range(1, n+1):
        print(i)
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")

# Keeps asking for valid user input
while True:
    try:
        num = int(input("Enter integer: "))
        break
    except:
        print("ERROR, ENTER INTEGER")

fizz_buzz(num)