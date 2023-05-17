import time
import pyotp

# Generate a random secret key
secret = pyotp.random_base32()

# Create a TOTP instance with the secret key
totp = pyotp.TOTP(secret)

# Get the current time in seconds
current_time = int(time.time())

# Calculate the OTP for the current time
otp = totp.at(current_time)

# Print the OTP generated
print("OTP:", otp)


#input the otp

input_code = input("Enter code : ")

print(totp.verify(input_code))
