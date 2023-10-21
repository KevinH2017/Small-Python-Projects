# Unit Converter (Temp, Currency, Volume, Mass)

# Fahrenheit to Celsius     C = (F - 32) / 1.8
def fah_to_cel():
    while True:
        try:
            user_fahrenheit = float(input("Input Fahrenheit(°F): "))
            new_celsius = (user_fahrenheit - 32) / 1.8
            print(user_fahrenheit, "°F is", new_celsius, "°C")
            break
        except:
            print("ERROR, ENTER NUMERIC VALUE!")

# Celsius to Fahrenheit     F = C * (9/5) + 32
def cel_to_fah():     
    while True:
        try:
            user_celsius = float(input("Input Celsius(°C): "))
            new_fahrenheit = user_celsius * (9/5) + 32
            print(user_celsius, "°C is", new_fahrenheit, "°F")
            break
        except:
            print("ERROR, ENTER NUMERIC VALUE!")

# Ounce to gram             Gram = Ounce * 28.3495
def ounce_to_gram():
    while True:
        try:
            user_ounce = float(input("Input Ounce(s)(oz): "))
            new_gram = user_ounce * 28.34952
            print(user_ounce, "oz is", new_gram, "g")
            break
        except:
            print("ERROR, ENTER NUMERIC VALUE!")

# Gram to Ounce
def gram_to_ounce():
    while True:
        try:
            user_gram = float(input("Input Gram(s)(g): "))
            new_ounce = user_gram / 28.34952
            print(user_gram, "g is", new_ounce, "oz")
            break
        except:
            print("ERROR, ENTER NUMERIC VALUE!")

# Galloon to Liters
def gal_to_liter():
    while True:
        try:
            user_gal = float(input("Input Gallon(s)(gal): "))
            new_liter = user_gal * 3.785412
            print(user_gal, "gal is", new_liter, "liters")
            break
        except:
            print("ERROR, ENTER NUMERIC VALUE!")

# Displays options for conversion
print("Python Unit Converter")
print("1 - Fahrenheit to Celsius")
print("2 - Celsius to Fahrenheit")
print("3 - Ounce to Gram")
print("4 - Gram to Ounce")
print("5 - Gallon to Liter")

while True:
    user_choice = input("Choose Converter: ")

    if user_choice == "1":
        fah_to_cel()
    elif user_choice == "2":
        cel_to_fah()
    elif user_choice == "3":
        ounce_to_gram()
    elif user_choice == "4":
        gram_to_ounce()
    elif user_choice == "5":
        gal_to_liter()
    

# Makes sure user inputs are valid
# while True:
#     user_choice = input("Choose Converter: ")
#     if user_choice == "1":
#         fah_to_cel()
#     elif user_choice == "2":
#         cel_to_fah()

#         # Asks user if they want to continue using the calculator, otherwise it will break
#         next_calc = input("Do you want to do another calculation? (y / n): ").lower()
#         if next_calc not in ("y", "n"):
#             next_calc = input("ERROR, PLEASE INPUT y OR n").lower()
#         elif next_calc == "y":
#             continue            # Restarts calculator
#         elif next_calc == "n":
#             print("Exiting Program...")
#             break               # Exits calculator