# Andres Soto Encoder File

def encoder(string):
    if string.isnumeric():
        encoded_string = ""
        for char in string:
            digit = int(char)
            digit = (digit + 3) % 10
            encoded_string += str(digit)
        return encoded_string


def decode(encoded_string):
    string = str(encoded_string)
    decoded_password = ""
    for char in string:
        digit = int(char)
        digit = (digit - 3 + 10) % 10
        decoded_password += str(digit)
    return decoded_password


while True:
    print("""\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit""")
    option = input("Please Enter an option: ")
    if option == "1":
        password = input("Please enter your password to encode: ")
        if len(password) == 8 and password.isnumeric():
            encoder(password)
            print("Your password has been encoded and stored!")
        else:
            print("Error! Enter 8 digit password")
    if option == "2":
        print(f"The encoded password is {encoder(password)}, and the original password is {decode(encoder(password))}")
    if option == "3":
        break
