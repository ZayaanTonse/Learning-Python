#Program:Internet speed category

print("=====INTERNET SPEED CHECKER=====")

speed=float(input("Enter your Internet speed(mbps): "))

if speed >= 100:
    print("category:Ultra-Fast")
elif speed >= 50:
    print("category:Fast")
elif speed >= 20:
    print("category:Moderate")
elif speed >0:
    print("category:Slow")
else:
    print("Invlid speed entered.")