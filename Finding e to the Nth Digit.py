# Finding e to the Nth Digit

import math

e_digit = int(input("Enter how many digits of Euler's number you would like to see (Max 53): ")) + 2
# print(math.e)     # 2.71828182845904509079559829842764884233474731445312

if e_digit > 55:
    print("ERROR, TOO MUCH, 53 MAXIMUM")
else:
    print("{:.{}}".format(math.e,e_digit))