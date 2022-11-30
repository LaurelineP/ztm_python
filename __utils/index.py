import re


def print_non_dunder(builtin):
	""" Print non dunder methods and attributes """
	try:
		for value in dir(builtin):
			if '__' not in value and re.match(r'^[a-zA-Z]', value):
				print(value, '\n')
	except:
		raise Exception('must provide argument')

