#Control Flow in Python

print("=====CONTROL FLOW IN PYTHON=====")

print("Control flow changes the order in which code executes.\n")

#Types of control flow
print("1. Conditional Statements-> if,elif,else")
print("2. Looping Statements    ->for,while")
print("3. Jump Statements       ->break,continue,pass\n")

#Example values
temperature =30
count =3
weather ="sunny"

#Conditional example
if weather =="Sunny":
    print("Bright day!")
elif weather == "rainy":
    print("Carry umbrella ")
else:
    print("Stay warm ")

#Looping examples
print("\nNumber1 to 5:")
for i in range (1,6):
    print(i,end=" ")

print("\nCountdwon:")
while count > 0:
    print(count, end=" ")
    count -=1

#Jump statements
print("\n\nJump statements demo:")
for i in range(1,6):
    if i ==2:
        continue
    if i ==4:
        break
    print("Number:",i)

#Pass example
for j in range(3):
    pass

print("\nControl Flow helps Python make decisions and repeat tasks.\n")