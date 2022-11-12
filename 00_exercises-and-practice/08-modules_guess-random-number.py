import sys
from random import random, randint

print(''' 
    Objective:
		Using the last seen built-in modules,
		create a program where from the terminal 
		one can pass arguments to generate a random 
		number and let the user being able to guess it
		--> write "stop" to stop the program
		
\t-----------------------------------------------------------------
\t-----------------------------------------------------------------
''')


def ask_random_number(expected_int):
	# random_value = round(random() * expected_int)
	random_value = randint(0, expected_int)
	message = f'\tGuess a value between 0 and {expected_int} ( included )? '

	guessed_value = None
	while guessed_value != random_value:
		# Provides insights to player
		feedback = ''

		is_exception = guessed_value == '' or guessed_value == 0

		if guessed_value or is_exception:
			# Handles feedback for edge cases [empty string or 0]
			if is_exception:
				feedback = guessed_value == 0 if 'Incorrect value' else 'Too low!'

			# Handles feedback for accepted cases [empty string or 0]
			elif guessed_value == 'stop':
				break
			elif guessed_value > expected_int:
				feedback = f'Above the limitation of {expected_int}'
			elif guessed_value < random_value:
				feedback = 'Too low!'
			elif guessed_value > random_value:
				feedback = 'Too high!'

			print(f'\t\tHint: {feedback}\n\t\tTry again 😛')
			print('\n\t---------------------------------------------')

		# Handle error cases or instruction to exit code on input value
		try:
			guessed_value = input(message)
			if guessed_value == 'stop':
				exit()
			else:
				guessed_value= int(guessed_value)
		except ValueError:
			print()
			guessed_value = ''

	return guessed_value


def trigger_guess_random_game():
	# set to 10 or get integer value
	try:
		expected_int = int(sys.argv[1], 10)
	except (IndexError, ValueError):
		expected_int = 10

	response = ask_random_number(expected_int)
	conclusion_message = f'	✨ The number to guess was {response}'
	print(conclusion_message)


trigger_guess_random_game()
