def main():
  lDuplicates = []
  isValid = True
  # Ask for first and last name
  sName = input("What is your first and last name? ")
  sInitials = sName[0] + sName[sName.find(" ")+1]
  # Ask for password
  sPassword = input("What is your desired password? ")
# ----------- CHECKING FOR ERRORS -----------------------

  # Check password length
  if len(sPassword) < 8 or len(sPassword) > 12:
    print(f"Password must be between 8 and 12 characters.")
    isValid = False
  # Check for "pass"
  if "pass" in sPassword.lower():
    print("Password cannot start with pass.")
    isValid = False
  # Check for uppercase letters
  if not any(letter.isupper() for letter in sPassword):
    print("Password must contain at least 1 uppercase letter.")
    isValid = False
  # Check for lowercase letters
  if not any(letter.islower() for letter in sPassword):
    print("Password must contain at least 1 lowercase letter.")
    isValid = False
  # Check for numbers
  if not any(letter.isdigit() for letter in sPassword):
    print("Password must have a number between 0 and 9")
    isValid = False
  # Check for special characters
  if not any(letter in "!@#$%^" for letter in sPassword):
    print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
    isValid = False
  # Check for initials
  if sInitials.lower() in sPassword.lower():
    print("Password must not contain user initials")
    isValid = False
  # Check to see if character appears more than once
  sPassword = sPassword.lower()
  if any(sPassword.count(letter) > 1 for letter in sPassword):
    isValid = False
    for char in sPassword:             
      if sPassword.count(char) > 1:
        if char not in lDuplicates:  
          lDuplicates.append(char)
    print("These characters appear more than once: ")
    for entry in lDuplicates:
      print(entry + ": " + str(sPassword.count(entry)) + " times")
#------------- END OF ERROR CHECKING ---------------------- 
  if isValid == True:
    print("Password is valid and OK to use.")
    
main()