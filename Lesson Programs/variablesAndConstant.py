#Python Program: Variables and Constant
#This program explians variable and Constant in Python

#VARIABLES
#Variables are used to store data values
#Python does not require explicit type decelaration

#Declaration
name="Alice"
age=21
height=5.6

print("variable-Name:",name)
print("variable-Age:",age)
print("variable-Height:",height)

#CONSTANTS
#Python does not have built-in constant types.
#By convention,we use UPPERCASE variable names for constants

PI=3.14159       #constant value for Pi
GRAVITY=9.8      #constant for gravitational acceleration
APP_NAME="MyApp" #constant for application name

print("\nConstant-PI:",PI)
print("\nConstant-GRAVITY:",GRAVITY)
print("\nConstant-APP_NAME:",APP_NAME)

#Technically constants CAN be changed in python(not enforced)
#but by convention we DO NOT change them
PI=3.14#This should not be done
print("\n(After modifying PI)PI:",PI,"->Not recommended!")

#Best Prsctice:treat uppercase names as constant and do not modify them