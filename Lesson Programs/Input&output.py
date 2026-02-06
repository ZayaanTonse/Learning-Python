#Python Program: Iput and Output

#-----Basic Print()-----
print("Hello,World!")
print("Numbers:",10,20,30)    #multiple values
print()   #black line

#-----print()with sep and end-----
print("A","B","C",sep="-")   #Custom seperator
print("Line without newline->",end=" ")
print("Continues Same line")

#-----Basic input()-----
name=input("\nEnter your name: ")
print("Hi," ,name+"!")

#-----Type casting-----
age=int(input("Enter your age:"))   #string->int
height=float(input("Enter height in meters: "))   #string->float
print("Age:",age,"|Height:",heigth)

#-----Multiple inputs-----
a,b=input("Enter two integers seperated by sapce: ").split()
a,b=int(a),int(b)
print("Sum=",a+b)

#-----Handling empty input-----
color=input("Favorite color(press Enter to skip): ").strip()
if color=="":
    color="Not provided"
print("Color:",color)

#-----Formatted output-----
item,price,qty="Book",120.5,2
print(f"Using f-string-> [ite],[price],[qty],Total=[price*qty:.2f]")

#-----Escape Sequemces-----
print("New line->\\n\ntab->\\t\tExample\tTab")