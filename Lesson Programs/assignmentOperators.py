# Assignment Operators in Python

print("\n=====ASSIGNMENTS OPERATORS IN PYTHON=====")

# Simple assignment
a = 10
print("Initial a =", a)

#Arithmetic assignment operators
a += 5     #Add and assign
a -= 3     #Substract and assign
a *= 2     #Multiply and assign
a /= 4     #Divide and assign
a *= 3     #Modulus assign
print("After various arthmetic assignments, a =", a)

#Floor division and exponent
a = 10
a //= 3
a **= 2
print("After floor division and exponent assignments, a =", a)

#Bitwise assignment operators
a = 5
a &= 3
a |= 2
a ^= 1
a <<= 1
a >>= 2
print("Final value after bitwise assignments, a =", a)

#User input example
x = int(input("\nEnter a number: "))
x += 10
x *= 2
x /= 5
print("Final x after assignment operations =", x)