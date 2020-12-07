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
	jsonWrite(rPInput, salt, uInput)


def jsonWrite(password, salt, username):
	from os import path
	import json

	if path.exists('potatoes.json'):
		past = json.load(open('potatoes.json', 'r'))
		print(past)
		print(type(past))
	else:
		open('potatoes.json', 'x')
		past = []
	past.append({
		'username': username,
		'password': password.hexdigest(),
		'salt': str(salt)
	})
	print(past)
	json.dump(past, open('potatoes.json', 'w+'))


def rmCombos():
	import os

	a0 = input('Are you sure you want to delete all username/password/salt combos? (Deletes potatoes.json) Type "YES" '
												'for confirmation:\nInput: ')
	if a0 != 'YES':
		exit(0)
	a1 = input(
		'Are you absolutely sure you want to delete all username/password/salt combos? Type "YES" again:\nInput: ')
	if a1 == 'YES':
		os.remove('potatoes.json')
