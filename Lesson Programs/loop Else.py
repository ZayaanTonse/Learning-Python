#Loop Else in Python

print("\n=====LOOP ELSE=====")

#for loop search example
nums =[2,4,6,8]
for i in nums:
    if i == 5:
        print("found 5")
        break
else:
    print("5 not found in list")

#while loop example
print()
x = 3
while x > 0:
    print(x,end=" ")
    x -=1
else:
    print("\nCountdown finished")

users=["Apple","Banana","Watermelon"]
target="Apple"
for user in users:
    print("User found")
    break

else:
    print("User not found")

print("\nElse runs only when loop completes without break.\n")