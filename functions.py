def login(username, password):
	uinput = input('Username >> ')
	if uinput not in username:
		exit('Invalid username. This incident will be reported.')

	pinput = input('Password >> ')
	if pinput != password[uinput]:
		exit('Incorrect password. This incident will be reported.')

	print('Valid credentials.')


def blakeGenPass():
	import os
	from hashlib import blake2b
	import json

	uInput = input('Username >> ')
	rUInput = input('Reenter Username >> ')
	if uInput != rUInput:
		exit('Usernames do not match')

	# TODO: implement customization
	# Obsolete
	# hashStrength = int(input('How many iterations of SHA-512 should be used for hashing? >> '))
	salt = os.urandom(16)
	pInput = blake2b(input('Password >> ').encode('utf-8'), salt=salt)
	rPInput = blake2b(input('Reenter Password >> ').encode('utf-8'), salt=salt)
	print('---NEWLINE---\n', pInput.hexdigest(), '\n---NEWLINE---\n', rPInput.hexdigest())
	if pInput.hexdigest() != rPInput.hexdigest():
		exit('Passwords do not match')
	try:
		open('potatoes.json', 'x')
	except FileExistsError:
		print('File already exists')
	with open('potatoes.json', 'r+') as jf:
		print(jf.read())
		try:
			print(jf.read())
			print(type(jf.read()))
			past = json.loads(jf.read())
			print(past)
			exit(0)
		except json.decoder.JSONDecodeError:
			print('No passwords saved yet, or corrupted file.')
			json.dump([{
				'password': rPInput.hexdigest(),
				'salt': str(salt)
			}], jf)

blakeGenPass()