#Python Keywords and Identifiers

import keyword #module to check python Keywords

#-------KEYWORDS-----
print("=== keywords in python===")
print("Some keywords are:", keyword.kwlist[:35]) #show first 10 keywords
print("Total numbers of keywords:", len(keyword.kwlist),"\n")

#Trying to use a keywords as variable( Wrong,will cause error of uncommented)
#if=10 #error,'if' is a keyword

#------IDENTIFIERS------
print("===Identifiers in python===")

#-------IDENTIFIER RULE SUMMARY-------
#1.An identifiers is a name used to identify a variable,function,class,etc.
#2. It can contian letter (A-2,a-2),digits (0-9),and underscores(_).
#3.IT MUST NOT start with a digit.
#4. It cannot be a python Keyword(reserved word).
#5. Use str.isidentifier() to check if a string is a valid identifier in python.

#Valid identifiers
name="Alice"    #letters
age1=21         #letter+digits
_student="John" #underscore at start
print ("Valididentifiers - >",name,age1,_student)

#Invalid identifiers ( Uncommenting will cause errors)
#2name="Bob"    #cannot start with a number
#my-name="Sam"  #hyphen not allowed
#class="Test"   #cannot use keyword

#Case sensitivity
city ="Mumbai"
City ="Delhi"
print("\ncity:",city)  #lowercase variable
print("City:",City)    #uppercase variable(different identifier)

#Identifier check using a python
print("\ncheck if a word is identifier or keyword:")
words=["name","2abc","class","value_1", "None"]
for w in words:
    print(w,"- > isidentifier?",w.isidentifier(),"| is keyword?", keyword.iskeyword(w))