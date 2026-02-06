#Program:Service Eligibility checker

print("=====SERVICE ELIGIBILITY CHECKER=====")

age=int(input("Enter your age: "))
citizen=input("Age you an Indian citizen? (yes/no):").lower()

if age >=18 and citizen =="yes":
    print("You are eligible to apply.")
else:
    print("Yoe are NOt eligible to apply.")