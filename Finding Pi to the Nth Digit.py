# Finding Pi to the Nth Digit

import math

pi_digit = int(input("Enter how many digits of pi you would like to see (Max 50): ")) + 2
# print(math.pi)      # 3.141592653589793115997963468544185161590576171875 is maximum input is 50

if pi_digit > 52:
    print("ERROR, TOO MUCH, 50 MAXIMUM")
else:
    print("{:.{}}".format(math.pi,pi_digit))
print("Finished, Closing...")