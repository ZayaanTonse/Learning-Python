#logical Operators in Python

print("\n=====LOGICAL OPERATORS IN PYTHON=====")

#Example values
a, b, c = 10, 20, 5
print("Using a =", a, "b =", b, ", c =", c, "\n")

#logical AND
print ("a > b or b > c->", (a > b) and (b > c))

#logical OR
print ("a > b or b > c ->",(a > b) or (b > c))

#logical NOT
print ("not(a > b) ->", not ( a> b))

#Combined expression
print ("(a > b) or (a < c and b > c) ->", (a > b) or ( a < c and b > c))

#Boolean value example
x, y= True, False
print("\nBoolean examples:")
print ("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not(x))

#User input example
num= int(input("\nEnter a number: "))

if num > 0 and num < 10:
    print("Number is between 1 and 9.")
elif num <= 0 or num >= 10:
         print("Number is not in the range 1-9.")
print("\nLogical operators: and / or / not \n")