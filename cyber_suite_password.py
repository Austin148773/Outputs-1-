import random
import string 
#Austin.White
#Date: 9/21/26
user_s = int (input("Enter a seed for the random number generation: "))
random.seed(user_s)
s_charter = random.choice("!@#$&(),-_")
low_1 = random.choice(string.ascii_lowercase)
up_1 = random.choice(string.ascii_uppercase)
low_2 = random.choice(string.ascii_lowercase)
up_2 = random.choice(string.ascii_uppercase)
num_1 = random.choice(string.digits)
num_2 = random.choice(string.digits)
s_charter_2 = random.choice("!@#$&(),-_")
print()
print("your random password is: ")
print(s_charter + up_1 + low_1 + low_2 + up_2 +num_1 + num_2 + s_charter_2)