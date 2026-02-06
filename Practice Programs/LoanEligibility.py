#Program:Loan Eligibility Check

print("=====LOAN ELIGIBILITY=====")

salary=float(input("Enter your monthly salary: "))
cibil=int(input("Enter your monthly CIBIL score: "))

if salary >=3000 and cibil >=700:
    print("Loan Approved")
else:
    print("Loan Rejected")