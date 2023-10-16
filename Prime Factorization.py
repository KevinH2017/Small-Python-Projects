# Prime Factorization
# 1) While n is divisible by 2, print 2 and divide n by 2. 

# 2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue. 

# 3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2. 

import math

def prime_fact():
    # User input to get an integer
    prime_num = int(input("Enter the number you want to find Prime Factors of: "))
        
    # Print the number of two's that divide n
    while prime_num % 2 == 0:
        print(2)
        prime_num = prime_num // 2              # Divides number to floor, lowest whole integer to avoid decimals
            
    # n must be odd at this point so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(prime_num))+1,2):
            
        # while i divides n, print i and divide n
        while prime_num % i== 0:
            print(i)
            prime_num = prime_num // i          # Divides number to floor, lowest whole integer to avoid decimals
                
    # Condition if n is a prime number greater than 2
    if prime_num > 2:
        print(prime_num)

prime_fact()