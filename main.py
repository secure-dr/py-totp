import pyotp
import qrcode

base32secret = pyotp.random_base32()
print('Secret: ', base32secret)

totp = pyotp.TOTP(base32secret)
top_uri = totp.provisioning_uri("test@test.com", issuer_name="MyTestApp")
print(top_uri)

img = qrcode.make(top_uri)
img.show()

inp = input("Enter the code from your app:")
print(totp.verify(inp))
