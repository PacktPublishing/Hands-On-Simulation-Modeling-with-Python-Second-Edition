import string
import random


char_set = list(string.ascii_letters + string.digits + "()!$%^&*@#")

password_length = int(input("How long should your password be?: "))

random.shuffle(char_set)
	
password = []
for i in range(password_length):
	password.append(random.choice(char_set))

random.shuffle(password)

print("".join(password))


