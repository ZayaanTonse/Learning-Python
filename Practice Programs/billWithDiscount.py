#Program: calculateTotal Bill with Discount

print("=====TOTAL BIL CALCULATOR=====")

#Takinginputs
productName=input("Enter the product name:")
price=float(input("Enter the price of one item:$"))
quantity=int(input("Enter the quantity:"))

#Calculating total price
total=price*quantity

#Applying discount(10% if total>1000)
discount=float(input("Enter the discount:"))
finalAmount=total-discount

print(f"\nProduct :{productName}")
print(f"Total price(before discount) :${total}")
print("Discount applied(10%):$",discount)
print("Final Bill Amount:$", finalAmount)