#Program:Swap Two Variables using a Temporary variable

print("=====SWAP TWO VARIABLES=====")

#Taking input
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("\nBefore swapping: a=", a,", b=", b)

#swapping using a temporary variable
temp = a
a = b
b = temp
print("After swapping: a=", a,", b=", b)