 
import sys
import random

cons = "bcdfghjklmnqrstvwxyz"
vows = "aeiou"
pass_len = int(sys.argv[1])
pass_count = int(sys.argv[2])

for i in range(pass_count):

	new_password = ""
	while len(new_password) < pass_len:
		new_password += random.choice(cons)
		new_password += random.choice(vows)

	new_password += str(random.randint(0,100))
	new_password = new_password.capitalize()

	print(new_password)
