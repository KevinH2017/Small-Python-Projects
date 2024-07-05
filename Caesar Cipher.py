# Caesar Cipher Encryption and Decryption
# Cannot take space character

# Encodes text with Caeser Cipher shifted s
def Caesar_Cipher_Encrypt(text, s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result

# Decodes text with Caeser Cipher shifted s
def Caesar_Cipher_Decrypt(text, s):
    result = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = text.upper()

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - s) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

text = input("Enter text: ")
s = int(input("How much to shift letters: "))
print("\nText: " + text)
print("Shift:", s)
print("Cipher: ", Caesar_Cipher_Encrypt(text, s))
print()

text_decrypt = input("Enter Encrypted text: ")
s_decrypt = int(input("How much to shift letters: "))
print("\nText: " + text_decrypt)
print("Shift:", s_decrypt)
print("Decrypted: ", Caesar_Cipher_Decrypt(text_decrypt, s_decrypt))        