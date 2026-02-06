#python Program:Boolean(bool)Data Type

import sys

#Declaration
is_active=True
is_verified=False

#Output
print("Value os is_active:",is_active)
print("Value of is_verified:",is_verified)

#Input
#Taking boolean input from user(entered as string'True' or'False)
user_input=input("EnterTrue or False:")
user_bool=user_input=="True"    #convert string to boolean
print("You entered:",user_bool)

#Type Checking
print("Type of is_active:",type(is_active))
print("Type if is_verfied:",type(is_verified))

#Type Casting
#int-> bool
print("Boolean from int(0):",bool(0))    #0 becomes True
print("Boolean from int(5):",bool(5))   #non-zero becomes True

#string->bool
print("Boolean from empty string:",bool(""))     #Empty string false
print("Boolean from'Hello':",bool("Hello"))      #Non-empty String is false

#float->bool
print("Boolean from float(0.0):",bool(0.0))     #0.0 is false
print("Boolean from float(3.14):",bool(3.14))   #Non-zero float is True

#Storage
print("Memory size of is_active:",sys.getsizeof(is_active), "bytes")
print("Memory size if is_verified:",sys.getsizeof(is_verified), "bytes")