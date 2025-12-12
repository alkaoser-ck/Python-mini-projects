from string import *
from random import *

# all ascii letters punctuations and digits
total = ascii_letters + punctuation + digits
# enter the legnth of the password
length = int(input())
# genarate a random password
password = ""
for i in range(length):
    password += choice(total)
# alt methode
# password = "".join(sample(total, length))
print(password)
