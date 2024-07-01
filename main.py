import random
import string

symbols = string.ascii_letters + string.digits + string.punctuation
password = str()
for i in range(21):
    password += random.choice(symbols)
print(password)
