import random
import string

letter= string.ascii_letters
num= "1234567890"
spe= "+!@#$%&*"

Rohit= letter+num+spe

Len=int(5)
password = "".join(random.sample (Rohit, Len ))

print(password)
