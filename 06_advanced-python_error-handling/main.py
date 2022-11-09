# ---------------------------------------------------------------------------- #
#                		   ERROR HANDLING	            			      	   #
# ---------------------------------------------------------------------------- #

print('''
-----------------------------------------------------------------------------------
				ERROR HANDLING
-----------------------------------------------------------------------------------
	Any errors breaks the running process of a python program
	Error handling are here to avoid having the code terminated by handling
	them accordingly: either loosely or specifically


	🔸 Errors:
	are the red lines that the terminal spits when a code is creating bugs
	📌 Error Exceptions are Python keywords referring to specific types of errors.
	https://docs.python.org/3/library/exceptions.html


	🔹 6 Common Errors Exceptions
	- `SyntaxError`:		when the code does not correspond to Python syntax.

	- `TypeError`: 			when a typography is made.

	- `NameError`: 			when the code uses a name reference but 
					which was never defined.

	- `ZeroDivisionError`:		when the code attempts to divide by zero.

	- `IndexError`: 		when the code tries to reach a list index 
					that does not exist.

	- `KeyError`:			when the code tries to reach a list index 
					that does not exist

-----------------------------------------------------------------------------------

🔸 Avoiding breaking code:
Error handling is how to handle unexpected cases to avoid having the code
to exit its own execution

Built in tools are provided in order to check those potential errors
which will be handle without exiting the program process:
( what is between squared brackets here, express that is optional )
	📌 Syntax: `try:` ... `except [<ErrorException>]:` ... [else:] ...[finally:]

		------------------------------------------------------
		Code in practice: Let's catch errors if a user provide
		a wrong number

		🔹 Have an input requesting the age
		🔹 Catch error when the user does not provide a
		correct age and ask the user again instead of 
		having a breaking error
''')

def ask_age():
	return int( input(f'''
		*******************************************************\n
		What is your age? '''
	))


''' Phase 1: Ask about the age
 	Ensured the value would be an integer / but an error will print on the console
  	if the user provide a word instead: 
	"ValueError invalid literal for int() with base 10: 'dede'" "
'''
# age = ask_age()




''' Phase 2: we understood that a breaking error is exiting the code;
	let's handle the error using by wrapping the code with `try: ... except:...`
'''
# try: 
# 	age = ask_age()
# 	print( age )
# except:
# 	print(' Please provide a valid age ')
# 	age = ask_age()




''' Step 3: the above code is not sufficient as a user may continue providing an 
	incorrect answer and it will end asking for the age.
	Let's use the while loop until getting the correct age
'''
def get_age():
	age = 0
	while not age:
		try:
			age = ask_age()
			if age == 0: raise ValueError('Incorrect age');
		except (ValueError) as err:
			print(f'''\t\tℹ️  Please provide a correct age. \n\t\t --> ❌ Error: {err}''')
		finally:
			message = f'✅ Ending process!' if age else '❌ Continuing process...'
			print( f'\t\t --> { message }')
	return age


age = get_age()

print(f'\t\t --> 🌟 Given age is: {age} \n\n')

