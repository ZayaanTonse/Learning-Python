#Relational (Comparision) Operators in Python

print("\n=====RELATIONAL OPERATORS IN PYTHON=====")

#Example values
a,b=10, 20
print ("Using a=", a, "and b=", b, "\n")

#Basic comparisions
print("a == b ->", a == b)   #equal to
print("a != b ->", a != b)   #not equal to
print("a > b ->", a > b)     #greater than
print("a < b ->", a< b)      #less than
print("a >= b ->", a >= b)   #greater or equal
print("a <= b ->", a <= b)   #less or equal

#User comparision example
x= int(input("\nEnter first number: "))
y= int(input("Enter second number: "))

print(x, "==", y, "->", x == y)
print(x, "!=", y, "->", x != y)
print(x, ">", y, "->", x > y)
print(x, "<", y, "->", x < y)
print(x, ">=", y, "->", x >= y)
print(x, "<=", y, "->", x <= y)

# String comparision demo
print("\nString comparision example:")
print("'apple' =='apple' ->", "apple" == "apple")
print("'apple' < 'banana' ->", "apple" < "banana")
print("'cat' > 'bat' ->", "cat" > "bat")