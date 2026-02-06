#python Program:Variables
#This program shows how variables work in python
#only basics:declaration,naming rules,reassingment,and output

#Rule 1: Variables store data values
name="Alice"
age=21
height=6.4

print("Name:", name)
print("Age:", age)
print("Height:", height)

#Rule 2:Variables can be reassinged (no need to declare type explicity)
age=22   # changed from 21
print ("\After reassignment,Age:",age)

##Rule 3:Variable name must start with a letter or underscore
_valid_name="this is valid"
print("\nAfter variable name example:",_valid_name)

#Rule 4:Vaiable names cannot start with a number or use special symbols
#2name="Not allowed"
#my-name="Not allowed"
#my_name="Allowed"
my_name="Alice Simith"
print("Variable with underscore:",my_name)

#Rule 5:Variables are case-sensitive
city="Mumbai"
City="Delhi"
print("\ncity:",city)
print("\nCity:",City)

#Rule 6:Multiple variables can be declared in one line
x,y,z=10,20,30
print("\nMultiple variables->x:",x,"y:",y,"z:",z)

#Rule 7:Same value to multiple variables
a = b = c ="Python"
print("Same value assigned->a:",a,"b:",b,"c:",c)