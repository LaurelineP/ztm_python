# ---------------------------------------------------------------------------- #
#                		   DECORATORS	            			      	  	   #
# ---------------------------------------------------------------------------- #
from time import time
def display_introduction():
	print('''
	-----------------------------------------------------------------------------------
					DECORATORS
	-----------------------------------------------------------------------------------
	🔸 Decorators... 
		- start with the character "@" before a name
		--> Examples: @classmethod, @staticmethod
	
		- bound to functions
		   They are powerful with functions 
		   ( Functions: being first class citizens can be passed around :
			like variables; as argument inside (HOC) functions )

		- supercharge a function ( gives a function extra features )

	''')

	def remind_function_passed_to_variable():
		print(f''' 	
		------------------- REMINDER: PASSING FUNCTION TO A VARIABLE -------------------

		🏗  Step 1: Defining function "greet"...''')
		def greet(): return ('Hello 👋')


		print(f''' 	📥 Step 2: Assigning function "greet" to a variable named "greet_in_variable"...''')
		greet_in_variable = greet


		print(f'''	🗑  Step 3: Deleting the function "greet"... ''')
		del greet


		# ( avoids breaking the code and exiting the code )
		result = ''
		try:
			result = greet()
		except NameError:
			print(f''' 	❌ Step 4: Executing "greet" does not work:
			--> Error: "Exception has occurred: NameError name "greet" is not defined"
			''')

		# greet() # will not work --> error Exception has occurred: NameError name 'greet' is not defined
		result = greet_in_variable()
		print(f''' 	✅ Step 5: Executing "greet_in_variable" does work
			( the function withing was not deleted as copied in variable
			before the function got deleted )
			--> result = {result}
			''')

	def remind_function_passed_to_a_function():
		print(f''' 	
		------------------- REMINDER: PASSING FUNCTION TO A FUNCTION -------------------

		🏗  Step 1: Defining function "execute_this_function_passed( func )"...''')

		def execute_this_function_passed( func ):
			func()
		
		print(f''' 	🏗  Step 2: Defining the function "say_hello()"...''')

		def say_hello():
			print('\t ---> Hello o o o o o 🙌')

		print(f''' 	📥 Step 3: Passing "say_hello" function as argument to "execute_this_function_passed"...''')
		execute_this_function_passed(say_hello)

	def go_through_decorators():
		print(f''' 	
		-------------------------------- DECORATORS --------------------------------
		Decorators super-charges to functions.
		Decorators are functions receiving function as parameters.
		Decorators once defined, are to be state right above the function which 
		should benefits from 

			Defining a decorator function allows to customize ( boost ) a function
			received as parameter(s).
		
			This works like wrapping function around the function destined to be 
			executed

			After defining like a regular function at first,
			this can be used as a keyword right above the other function we'd
			like to wrap
		-------------------------------------------------------------------------------
		Example:
				@use_decorator
				def return_hello():
					return 'H E L L O O O 🙌'
		-------------------------------------------------------------------------------

	
		''')

		def use_decorator( func ):
			def wrap_func():
				customization = f'''
				++++++++++++++++++++++++++++++++++
					{func()}
				++++++++++++++++++++++++++++++++++

				'''
				return customization
			return wrap_func


		@use_decorator
		def return_hello():
			return 'H E L L O O O 🙌'

		result = return_hello()
		print( '\t\t\t - Result using the defined decorator `@use_decorator`: \n', result )



		def return_hello():
			return 'H E L L O O O 🙌'
		result = return_hello()

		print( '\t\t\t - Result without decorator: ', result )

	def explain_why_decorators_are_needed():
		print(f''' 	


		----------------------------------------------------------------------------
		------------------------ WHY DO WE NEED DECORATORS -------------------------

		To enhance developer experience in avoiding repeated pattern or format to
		apply
		
		Let's create a @performance decorator in order to analyse how long a 
		function takes to execute

	
		''')
		def get_performance( func ):
			def wrap_function( *args ):
				t1 = time()
				result = func( args )
				t2 = time()
				print(f'Took { args } { t2 - t1 }s ')

				return result
			return wrap_function

		@get_performance
		def process_time_consuming_code( range_number = 0 ):
			print(f'Looping within a range of {range_number[0]} ...')
			for i in range(range_number[0]):
				i * 5

		process_time_consuming_code(100000000)

	remind_function_passed_to_variable()
	remind_function_passed_to_a_function()
	go_through_decorators()
	explain_why_decorators_are_needed()

		
display_introduction()
