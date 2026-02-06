#=====MEMBERSHIP OPERATORS IN PYTHON=====

#Membership operators help check if a value exsits inside sequences
#Operators : 'in' ->True if values exists
#            'not in'->True if value does NOT exist

#-----String Example-----
text="python programming"
print("'p' in text:", 'p' in text)
print("'java' not in text:", 'java' not in text)

#----List Example----
fruits=["apple","banana","cherry"]
print("'banana' in fruits:", 'banana' in fruits) #element exists

#----Tuple Example----
nums =(10,20,30)
print("20 in nums:", 20 in nums) #tuple membership checks

#----Dictionary Example----
students = {"name":"John","age":23}
print("'name' in students:", 'name'in students) #Check keys only

#-----Set Example-----
word=input("Enter a word:")
print("'Yellow' not in colors:", 'yellow' not in colors)   #fast lookup

#-----User Input Example-----
word=input("Enter a word:")
if 'a' in word:          #checking character presence
    print("The letter 'a' is present.")
else:
    print("The letter 'a' is not present.")

print("\nUse'in' or 'not' to test membership in strings,lists,tuples,sets, and dictionary.")