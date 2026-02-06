#Program:Check OTP matches or not

print("=====OTP VERIFICITION=====")

correctOtp="5678"
attempts=""

#Keep asking until matching OTP
while attempts !=correctOtp:
    attempts=input("Enter OTP:")

print("OTP verified successfully.")