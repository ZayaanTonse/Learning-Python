#Program: calculate car fuel Efficiency(Mileage)

print("=====CAR MILEAGE CALCULATOR=====")

#Inputs from user
distance=float(input("Enter total distance traveled(in km): "))
fuelused=float(input("Enter fuel used(in liters)" ))

#Mileage calculation
mileage=distance/fuelused

print(f"\nYour car's mileage is {mileage} km/litre")