#IF-ELSE Statement in Python

print("\n=====IF-ELSE STATEMENT IN PYTHON=====")

#Even or odd
n=int(input("Enter a number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

#Voting eligiblity
age=int(input("\nEnter age: "))
if age >=18:
    print("Eligible")
else:
    print("Not eligible")

#Compare numbers
a=int(input("\nEnter first number: "))
b=int(input("Enter second number: "))
if a > b:
    print("First is greater")
else:
    print("Second is greater or equal")

print("\nIF-ELSE executes only one block.\n")