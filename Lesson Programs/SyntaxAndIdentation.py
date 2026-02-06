#Python Syntax&Identaion
#This program explains the rules of syntax and Identation in python

#BASIC SYNTAX
#python program are written using statements
#Each statements usually goes on a new

print("Hello,World!")   #Example of a simple python statements

#Multiple statements can be written on the same line using;
x=10;y=20; print("x:",x,"y:",y)

#IDENTATION
#Identation(spaces at the beginning of a line) defines code blocks in python
#Unlike other language(c,Java)that use {},Python uses identation

age=18
if age>=18:    #Correct identation
    print("\nyou are an adult.")    #4spaces identation
    print("You can vote.")
else:
    print("You are a minor.")

#Wrong identation(would cause an Identation Error if uncommented):
#if age>=18:
#print("this will cause an error")

#IDENTATION LEVELS
#Nested blocks requires extra identation
number=10
if number>0:
    print("\nNumber is positive")
    if number%2==0:
        print("It is also even")#moreidentation for nested block
    else:
        print("It is odd")
else:
     print("Number is negative")

#IDENTATION CONSISTANCY
#Always use the SAME number of spaces (PEP8 recomands4)
#Mixing tabs and spaces causes errors.

#COMMENTS
#Single-line commentusing#
"""
This is a multi-line comment
written inside triple quotes.
"""

#LINE CONTINUATION
#If a statements is too long,use\to continue on next line
long_variable_name=100+200+300+\
                   400+500
print("\nLine continuation result:",long_variable_name)

#Paretheses,brackets,and braces allow implict line continuation
numbers=[
    1,2,3,
    4,5,6
]
print("Numbers list:", numbers)
