#Andres Soto Encoder File
def encoder(string):
    if string.isnumeric():
        encoded_string = " "
        for char in string:
            digit = int(char)
            digit = (digit + 3) % 10
            encoded_string += str(digit)
        return encoded_string
def main():
    while True:
        print("""Menu\n-------------\n1. Encode\n2. Decode\n3. Quit""")
        option = input("Please Enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isnumeric():
                encoder(password)
                print("Your password has been encoded and stored!")
            else:
                print("Error! Enter 8 digit password")

        if option == "3":
            break
if __name__ == "__main__":
    main()

