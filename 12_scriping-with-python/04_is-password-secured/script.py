import sys
import requests # https://pypi.org/project/requests/
# from __utils.index import print_non_dunder
import hashlib


sys.path.append('../../__utils')

print('''
	🔸 Checks if a password is safe and secured
	If it is a hacked password or not
	dictionary attack : massive attack accross all items
''')


# checking key anonymy

print('''
	🔸 key anonymity: with 5 first characters from hashed pwd,
	 api would check list of leaked passwords.
	 Using key anonymity would be the secured way to check password
	 without providing the full one
	 
	 Hash functions are algorithms to transform a string into a non 
	 friendly string.
	 
	 This is meant to make it harder for a middle man to clearly see 
	 a password. From an hashed password it is not possible to find the
	 original password
	 
	 Passing the same input ( string ) to the hash functions would always
	 returns the same value ==> this is called "idempotent" 
	 ( a function receiving a same input, will always return the same output ) 
	 ''')


def hash_password(clear_password):
	""" check if password exists in API response """
	# 0. encode the has
	pwd_utf8 = clear_password.encode('utf-8')

	# 1. format the text ( hexdigest, and upper )
	sha1password = hashlib.sha1(pwd_utf8).hexdigest().upper()

	# 2. gets the 5 characters ( and avoid sharing the
	# entire hash for security reason practice )
	# sha1password_short = sha1password[0:5]
	print('---sha1password', sha1password)
	return sha1password


def read_response(res):
	# returns all the hashed hacked <FULL-HASH>:<HACKED_COUNT>
	# return res.text.split('\r\n')
	return res.text.splitlines()


def check_password_leeked_count(password):
	# https://haveibeenpwned.com/Passwords

	# 1. gets hashed password encoded
	sha1_password = hash_password(password)
	sha1_short, sha1_tail = sha1_password[:5], sha1_password[5:]

	# 2. request the api for the
	url = f'https://api.pwnedpasswords.com/range/{sha1_short}'
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching data: {res.status_code}')

	# 3. gets response content details
	hash_list = read_response(res)
	hashes = (line.split(':') for line in hash_list)
	for h, c in hashes:
		if h == sha1_tail:
			return c
	return None


# https://codebeautify.org/sha1-hash-generator


def main(args):
	for arg in args:
		count = check_password_leeked_count(arg)
		if not count:
			print(f'✅The "{arg}" was not found ')
		else:
			print(f'❌ The password "{arg}" has been found { count } times ')
	return '---- Check done!'


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))