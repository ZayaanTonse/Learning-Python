#Program:Temperature Converter

print("=====TEMPERATURE CONVERTER=====")

def c_to_f(c):
    return (c *9/5)+32

def f_to_c(f):
    return (f -32)*5/9

choice=input("Convert (c/f): ").upper()

if choice =="C":
    c=float(input("Enter Celsius:"))
    print("Fahernheit:",c_to_f(c))

elif choice =="F":
    f=float(input("Enter Fahernheit:"))
    print("Celsius:",f_to_c(f))

else:
    print("Invalid option")