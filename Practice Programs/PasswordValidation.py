#Program=Password Validators

print("=====PASSWORD VALIDATOR=====")

password=input("Enter password:")

#Validation rules
hasDigit=any(ch.isdigit()for ch in password)
hasUpper=any(ch.isupper()for ch in password)
hasLower=any(ch.islower()for ch in password)
hasSpecial=any(ch in"!@#$^&*()-_=+[]{};:/?,.<>"for ch in password)
hasLength=len(password) >=8

#check all conditions
if hasDigit and hasUpper and hasLower and hasSpecial and hasLength:
    print("Password is strong and valid.")
else:
    print("Weak password.Must include:")
    print("-At least 8 characters")
    print("-At least one digit")
    print("-At least one uppercase letter")
    print("-At least one lowercase letter")
    print("-At least one special character(!@#$ etc.)")