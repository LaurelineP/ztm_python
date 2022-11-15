import re

print(''' 
    Objective:
    Using RegExp, check the password correctness
    - password must have 8 or more characters
    - password can contain any character ( lower, upper case,
    digit, symbols [ $@# ...] 
    - password have to end with a digit

\t-----------------------------------------------------------------
\t-----------------------------------------------------------------
''')


def is_valid_password(pwd):
	pattern = re.compile(r'((\w|\W|$){8,})\d$')
	try:
		full_match = pattern.fullmatch(pwd)
		return full_match is not None
	except:
		return False


def request_password():
	password = None
	while True:
		if not password:
			_password = input('\n\t\t🔸Please, provide a new password ( minimum 8 characters ): ')

			is_valid = is_valid_password(_password)
			message = f'✅  Valid password: {_password}' if is_valid else '❌  Invalid password'
			password = _password if is_valid else None
			print(f'\t\t\t {message}\n')
			if password:
				return password
		continue


request_password()

