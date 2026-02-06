#Program:ATM Withdrawl Simulator

print("=====ATM WITH SIMLUATOR=====")

balance=5000

#Loop until user enters valid amount
while True:
    amt=int(input("Enter amount to withdraw:"))

    if amt <=0:
        print("Invalid amount Try again.")
    elif amt > balance:
        print("Insufficient balance.")
    else:
        balance-=amt
        print("Withdrawl successfull.Remaining balance:",balance)
        break