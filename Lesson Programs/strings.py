# Strings in Python

#Creating strings
s1="Python"
msg="""Learning
Strings in Python"""

print(s1)
print(msg)

#Indexing & slicing
print(s1[0], s1[-1])        #First&last char
print(s1[1:4], s1[::-1])    #slice&reverse

#Useful methods
t=" Hello Python "
print(t.strip(),t.lower(),t.replace("Python","Java"))

#Formatting
name,age="John",23
print(f"{name}is{age}years old")                   #F-string
print("Name:{},Age:{}".format(name, age))    #format()