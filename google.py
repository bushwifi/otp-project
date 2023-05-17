import time
import pyotp
import qrcode


key = "cookiesaregood"

uri=pyotp.totp.TOTP(key).provisioning_uri(name="mikesmith"
                                               ,issuer_name="bush app")
print(uri)


qrcode.make(uri).save("totp.png")
