import time
import pyotp

key="NeuralNinemysecret"

counter=0

hopt = pyotp.HOTP(key)

print(hopt.at(0))
print(hopt.at(1))
print(hopt.at(2))
print(hopt.at(3))
print(hopt.at(4))
print(hopt.at(5))


for _ in range(5):
    print(hopt.verify(input("enter code:"),counter))
    counter += 1