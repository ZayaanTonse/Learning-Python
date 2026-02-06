#Program:Login system with 3 Attempts

print("=====LOGINSYSTEM=====")

password="admin1223"
attempts=3

#User gets 3 tries
while attempts > 0:
    entered=input("Enter password: ")

    if entered == password:
        print("Login successful.")
        break
    else:
        attempts -=1
        print("Account locked.Try again later.")