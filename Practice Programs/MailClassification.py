#program:Extract only gmail accounts

print("=====FILTER GMAILACCOUNTS=====")

#Email list
emails=[
    "john@gmail.com","rita@yahoo.com","alex@gmail.com",
    "tom@outlook.com","sara@gmail.com"
]

print("Gmail users:")
#print only emails ending with Gmail domain
for email in emails:
    if email.endswith("@gmail.com"):
        print(email)