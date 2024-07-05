# Mortgage Calculator
# Calculates the monthly payments of a fixed term mortgage over Nth terms at a given interest rate
# Calculates how long it would take for the user to pay back the loan

# Mortgage formula
# M = P * (r * (pow((1 + r), n)) / (pow((1 + r), n) - 1))

# Compounding Interest formula
# CI = P * pow(((1 + r) / n), n * t)

def mortgage_calc():
    p = int(input("Principle Amount: "))
    r = float(input("Yearly Interest Rate: "))
    n = int(input("Number of payments a year: "))
    # t = int(input("How many years you'll have the mortgage: "))

    mort_formula = p * ((r * pow((1 + r), n)) / (pow((1 + r), n) - 1))
    # mort_formula = p * (r * (1 + r) ** n) / (((1 + r) **n) -1)
    mortgage_string = '{:,.2f}'.format(mort_formula) 
    print(mort_formula)

    # comp_interest = p * pow(((1 + r) / n), (n * t))
    # comp_interest = p * ((1 + r) / 2) ** (n * t)
    # print(comp_interest)
    # comp_interest_string = '{:,.2f}'.format(comp_interest) 
      

    print("Monthly payments is estimated to be about $" + mortgage_string)
    # print("Compounding Interest is estimated to be about $" + comp_interest_string)
    # formula = 4000 * (1 + 0.02 / 2) ** (2 * 4)
    # print(formula)

mortgage_calc()