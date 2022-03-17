def main():
  lstDuplicates = []
  isValid = True
  hasUpper = False
  hasLower = False
  hasDigit = False
  hasSpecialChar = False
  hasDuplicate = False
  # Ask for first and last name
  sName = input("What is your first and last name? ")
  sInitials = sName[0] + sName[sName.find(" ")+1]
  # # Ask for password
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

  # Iterate over the password
  for char in sPassword:
    # Check for uppercase letters
    if char.isupper():
      hasUpper = True  
    # Check for lowercase letters   
    if char.islower():
      hasLower = True
    # Check for numbers
    if char.isdigit():
      hasDigit = True
    # Check for special characters
    if char in "!@#$%^":  
      hasSpecialChar = True
  # Check to see if character appears more than once
    sPassword = sPassword.lower() 
    if sPassword.count(char) > 1:
      hasDuplicate = True
      if char not in lstDuplicates:
        lstDuplicates.append(char)
          
  # Print if uppercase char needed
  if not hasUpper:
    print("Password must contain at least 1 uppercase letter.")
    isValid = False
  # Print if lower case char needed
  if not hasLower:
    print("Password must contain at least 1 lowercase letter.")
    isValid = False
  # Print if no number present
  if not hasDigit:
    print("Password must have a number between 0 and 9")
    isValid = False
  # Print if no special char
  if not hasSpecialChar:
    print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
    isValid = False
  # Check for initials
  if sInitials.lower() in sPassword:
    print("Password must not contain user initials")
    isValid = False 
  # Print Duplicate Chars
  if hasDuplicate: 
    print("These characters appear more than once: ")
    isValid = False
    for entry in lstDuplicates:
      print(entry + ": " + str(sPassword.count(entry)) + " times")

# #------------- END OF ERROR CHECKING ---------------------- 
  if isValid:
    print("Password is valid and OK to use.")
      
main()
