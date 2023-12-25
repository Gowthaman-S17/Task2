import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    

    print(f"OTP sent to {receiver_email}: {otp}")

def verify_otp(user_entered_otp, otp):
    return user_entered_otp == otp


otp = generate_otp()
user_email = input("Enter your email address: ")
send_otp_email(user_email, otp)
user_entered_otp = input("Enter the OTP sent to your email: ")

if verify_otp(user_entered_otp, otp):
    print("OTP verification successful. User verified!")
else:
    print("Incorrect OTP. Verification failed.")
