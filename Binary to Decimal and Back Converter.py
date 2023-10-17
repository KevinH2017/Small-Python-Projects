# Binary to Decimal and Back Converter

# Converts decimal to binary
def dec_to_bin():
    # Keeps prompting for correct input
    while True:
        try:
            user_dec = int(input("Decimal: "))
            print(bin(user_dec)[2:])                    # Removes '0b' from beginning  
        except ValueError:
            print("ERROR, INPUT DECIMAL VALUE, EX: 42")
        else:
            break

# Converts binary to decimal
def bin_to_dec():
    # Keeps prompting for correct input
    while True:
        try:
            user_bin = input("Binary: ")
            print(int(user_bin, 2))                     # Converts binary to integer
        except ValueError:
            print("ERROR, INPUT BINARY VALUE, EX:1101")
        else:
            break    

def user_convert():
    # User input for b or d
    dec_or_bin = str(input("Binary (b) or Decimal (d): ")).lower()
    print(dec_or_bin)

    # Keeps asking user for input b or d
    while True:
        if dec_or_bin not in ("b", "d"):
            dec_or_bin = str(input("Error enter b or d: ")).lower()

        # Takes user input to convert binary to decimal, or decimal to binary, breaks while True after conversion
        elif dec_or_bin == "b":
            bin_to_dec()
            break
        elif dec_or_bin == "d":
            dec_to_bin()
            break

user_convert()