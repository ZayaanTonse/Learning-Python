#Program:Calculate discount on the given price of purchase

print("=====DISCOUNT ON PRICE AMOUNT=====")

amount=float(input("Enter purchase amount: "))

if amount >=5000:
    print("You get a 20% dicount.")
elif amount >=3000:
    print("You get a 10% dicount.")
elif amount >=1000:
    print("You get a 5% dicount.")
else:
    print("No discount.")