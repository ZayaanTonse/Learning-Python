#Conditional Statements in Python -IF

print("\n=====IF STATEMENT IN PYTHON=====")

#Example 1:basic IF
age=int(input("Enter your age: "))
if age >=18:
    print("Eligible to vote.")

#Example 2:temperature check
temp=float(input("\nEnter temperature: "))
if temp>30:
    print("It's hot today.")

#Example 3:boolean condition
is_student=True
if is_student:
    print("\nStudent discount available.")

#Example 4:independent IFs
marks =int(input("\nEnter marks: "))
if marks >=90:print("GradeA+")
if marks >=75:print("GradeA")
if marks >=60:print("GradeB")
if marks >=40:print("GradeC")
if marks < 40:print("Fail")

#Example 5:even/odd
num=int(input("\nEnter a number: "))
if num % 2 ==0:print("Even number")
if num % 2 !=0:print("Odd number")

print("\nIf execute only when condition is True.\n")