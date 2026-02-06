#Dictionaries in Python

#Creating dictionaries
student={"name":"Aditiya","age":23,"course":"CS"}
person=dict(name="Sneha",age=21)
empty={}
school={"s1":{"name":"Asha","marks":82}}

print(student,person,empty,school)

#Accessing values
print(student["name"])
print(student.get("course"))
print(student.get("phone","Not Provided"))

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

#Adding & updating
student["phone"]="98675"
student["age"]=24
student.update({"city":"Pune"})
student.setdefault("dept","Engineering")
print(student)

#Removing elements
student.pop("phone",None)
student.popitem()
if"city" in student:
    del student["city"]
print(student)

#Iterating
emp={"id":101,"name":"Rina","role":"Engineer"}
for k in emp:print(k)
for v in emp.values():print(v)
for k,v in emp.items():print(k,v)

#Nested dictionary access
company={"d1":{"manager":"Amit"}}
print(company["d1"]["manager"])

#Frequency counter(short)
text=input("Enter text: ").split()
freq={}
for w in text:
    freq[w]=freq.get(w, 0)+1
print(freq)