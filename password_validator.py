# Password Validator

#Function that gets inputted name's initials


def get_initials():
    name = input("What is your first and last name?: ")
    initials = ""
    for char in name:
    #check uppercase characters
        if char.isupper():
            initials += char
    return print(initials)

#Function that checks and validates the password
def check_password():
    password = input("What is your desired password? ")
    get_four_char = password[0:4].lower()
    length_password = len(password)
    i = True
    while i:
        if length_password < 8 or length_password > 12:
            print("Password must be between 8 and 12 characters")
            check_password()
        if get_four_char == "pass":
            print("Password cannot start with Pass")
            check_password()
        else:
            i = False
        for char in password:
            if char.isupper():
                print("IT WORKS")
                break
            else:
                print("Password must contain at least 1 uppercase letter")
                break

get_initials()
check_password()



