def login(username, password):
	uinput = input('Username >> ')
	if uinput not in username:
		exit('Invalid username. This incident will be reported.')

	pinput = input('Password >> ')
	if pinput != password[uinput]:
		exit('Incorrect password. This incident will be reported.')

	print('Valid credentials.')


def genPass():
	import os
	import hashlib

	uInput = input('Username >> ')
	rUInput = input('Reenter Username >> ')
	if uInput != rUInput:
		exit('Usernames do not match')

	hashStrength = int(input('How many iterations of SHA-512 should be used for hashing? >> '))
	salt = os.urandom(128)
	pInput = input('Password >> ')