import random as ran
import string as stg

pass_len = 12
charValues = stg.ascii_letters + stg.digits + stg.punctuation 
password = ""

for i in range(pass_len):
    password += ran.choice(charValues)

print("your random password is:", password)
