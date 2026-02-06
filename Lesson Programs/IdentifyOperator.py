#Identify Operators in Python

print("\n=====IDENTITY OPERATORS IN PYTHON=====")

#Integers
a, b =10, 10
print("a =", a, "b =", b)
print("a == b ->", a == b)
print("a is b ->", a is b)
print("a is not b ->", a is not b, "\n")

#Strings
x, y="hello", "hello"
print("x =", x, "y =", y)
print("x == y ->", x == y)
print("x is y ->", x is y, "\n")

#Lists (mutable objects)
list1= [1,2,3]
list2=[1,2,3]
print("list1 == list2 ->", list1 == list2)
print("list1 is list2 ->", list1 is list2)
print("list1 is not list2 ->", list1 is not list2, "\n")

#None comparision
val=None
print("val is None ->", val is None)
print("val is not None ->", val is not None, "\n")

#Memory check
num1, num2, num3, num4=256 ,256, 300, 300
print("num1 is num2 ->", num1 is num2)
print("num2 is num3 ->", num2 is num3)

print ("\nUse 'is' for identify and '==' porvalue comparision.\n")