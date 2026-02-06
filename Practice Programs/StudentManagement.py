#Program:Student Manager

print("=====STUDENT MANAGER=====")

students=[]

def add_students(name,age):
    students.append({"name":name,"age":age})

def display_students():
    for s in students:
        print(s["name"],"-",s["age"])

while True:
    print("\n1.Add student \n2 veiw students\n3Exit")
    ch=int(input("Choose option:"))

    if ch ==1:
        name=input("Name:")
        age=int(input("Age:"))
        add_students(name,age)

    elif ch == 2:
        display_students()

    elif ch == 3:
        break

    else:
        print("Invalid choice.")