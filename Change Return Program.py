# Change Return Program
# User enters amount of money and this program will return the number of quarters, dimes, nickles, and pennies needed

def change_return():
    money = float(input("Enter Money: "))     
    money_string = '{:,.2f}'.format(money)      # Formats money to have 2 decimal places

    print("$" + money_string)
    print("Your change is:")

    quarters, money = divmod(money, 0.25)       # divmod returns a tuple containing the quotient and the remainder when money is divided by 0.25
    print(int(quarters), "quarters")            # int is used to pritn whole numbers
    money = round(money, 2)                     # Rounds money to 2 decimal places, to avoid trailing 9s

    dimes, money = divmod(money, 0.10)
    print(int(dimes), "dimes")
    money = round(money, 2)

    nickels, money = divmod(money, 0.05)
    print(int(nickels), "nickels")
    money = round(money, 2)

    pennies = round(money / 0.01, 0)            # Rounds money to get last 2 decimal places to be divided by 0.01 
    print(int(pennies), "pennies")

change_return()