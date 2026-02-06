#Program to calculate the volume of a cylinder
import math

cylinderRadius=float(input("Enter the radius of the cylinder(in units): "))
cylinderHeight=float(input("Enter the height of the cylinder(in units): "))

#volume formula:pi*r^2*h
volume=math.pi*cylinderRadius**2*cylinderHeight

print("The volume of the cylinder is:",round(volume, 2), "cubic units")