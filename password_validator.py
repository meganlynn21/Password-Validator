# Password Validator

#Gets inputted name's initials

from os import dup


name = input("What is your first and last name?: ")
initials = ""
for char in name:
#check uppercase characters
    if char.isupper():
        initials += char
print(initials)

#Function that checks and validates the password
def main(min_len: int, max_len: int):
    duplicates = []
    special_char = "!@#$%^"
    #Check password input and return password string.
    while True:
        password = input("What is your desired password? ")
        
        # -------------------- Check for Bad Inputs -------------------- #
        # Check for characters that repeat more than once and count how many times they appear
        for char in password:
            if password.count(char) > 1:
                duplicates.append(char)
        print(f"The characters {char} appears {len(duplicates)} times")
        main(8,12)

        # Check for input.
        if not password:
            print("Please enter a password.\n")
            continue
        
        # Check if initials are in password
        elif initials.lower() in password or initials.upper() in password:
            print("Password must not contain user initials")

        # Check for weak password.
        elif "pass" in password or "Pass" in password:
            print("Password cannot start with pass.\n")
            continue

        # Check for length.
        elif min_len < len(password) < max_len:
            print(f"Password must be between {min_len} and {max_len} characters.\n")
            continue

        # Check for Uppercase letters
        elif not any(letter.isupper() for letter in password):
            print("Password must contain at least 1 uppercase letter.\n")
            continue

        # Check for lowercase letters
        elif not any(letter.islower() for letter in password):
            print("Password must contain at least 1 lowercase letter.\n")
            continue

        # Check if there is at least one number between 0 and 9
        elif not any(letter.isdigit() for letter in password):
            print("Password must have a number between 0 and 9")

        # Check for special characters
        elif not any(letter in special_char for letter in password):
            print("Password must contain a special character")

        # -------------------- End of Bad Inputs -------------------- #
        
        else:
            return password


main(8,12)



