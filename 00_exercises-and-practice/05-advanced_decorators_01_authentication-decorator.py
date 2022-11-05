print('''
—--------------—--------------—--------------—--------------—--------------—--------------
	Objective: 
		For the given code provide an @authenticated decorator
		to enable user1 with 'valid' attribute set to True
		Extra: implement the whole concept in your own way

	—--------------—--------------—--------------—--------------
			PERSONAL IMPLEMENTATION FROM SCRATCH
''')

def is_authorized( fn ):
	def wrapper( *args ):
		_self = args[0]
		sentence_alternative = 'authorized' if _self.is_valid else 'not authorized'
		if _self.is_valid:
			return f'{_self.name}: {fn(_self)}'
		return f'{ _self.name } is {sentence_alternative} to send a message.'
	return wrapper



class User:
	def __init__(self, name, is_valid):
		self.name = name
		self.is_valid = is_valid

	@is_authorized
	def message_text( self ):
		return 'Hello, How are you ?'




user1 = User('Ezra', False)
user2 = User('Azra', True)

result_user1 = user1.message_text()
result_user2 = user2.message_text()



print(f'''
		User 1 has `is_valid` to `False` 
			- result: {result_user1}

		User 2 had `is_valid` to `True` 
			- result: {result_user2}
		
		Exo link: https://repl.it/@aneagoie/decorators2-exercise
		Solution link: https://repl.it/@aneagoie/decorators-1

	—--------------—--------------—--------------—--------------	
	—--------------—--------------—--------------—--------------	
''')


# ------------------------------------
# CODE PROVIDED INITIALLY
# Create an @authenticated decorator that only allows the function to run 
# is user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
	# code below
	def wrapper(user):
		if user["valid"]:
			fn(user)
		else:
			print( f'\t\t\t{ user["name"] } is not authorized to send a message!')
	return wrapper

@authenticated
def message_friends(user):
    print( f'\t\t\t Message has been sent')

print(f'''
		Given exercise implementation:
		Here the user dictionary has `is_valid` set to `False`

		Result:
''')
print(  message_friends(user1) )

print('—--------------—--------------—--------------—--------------—--------------—--------------')
