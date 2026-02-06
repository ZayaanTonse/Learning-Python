#IF-ELIF-ELSE ladder in Python

print("\n=====IF-ELIF-ELSE LADDER=====")

#Grading example
marks=int(input("Enter marks: "))

if marks >=90:
    print("GradeA+")
elif marks >=75:
    print("GradeA")
elif marks >=60:
    print("GradeB")
elif marks >=40:
    print("GradeC")
else:
    print("Fail")

#Temperature example
temp=float(input("\nEnter temperature: "))

if temp >35:
    print("Too hot")
elif temp >25:
    print("Warm")
elif temp >15:
    print("Pleasent")
elif temp >5:
    print("Clod")
else:
    print("Freezing")

print("\nOnly one block runs based on the first True condition.\n")