#Program:Simple Intrest Calculator

print("=====SIMPLE INTREST CALCULATOR=====")

#Formula=SI=(P * R * T)/100
principal=float(input("Enter principal Amount($):"))
rate=float(input("Enter rate of Intrest(%):"))
time=float(input("Enter Time (in years):"))

simpleIntrest=(principal*rate*time)/100

print("\nprincipal Amount:$",principal)
print("Rate of Intrest:",rate,"%")
print("Time:",time,"years")
print("Simple Intrest:$",SimpleIntrest)
print("Total Amount after intrest:$",principal+simpleIntrest)