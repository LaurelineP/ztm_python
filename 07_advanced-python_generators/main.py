# ---------------------------------------------------------------------------- #
#                		   		GENERATORS	            			      	   #
# ---------------------------------------------------------------------------- #

print('''
-----------------------------------------------------------------------------------
				GENERATORS
-----------------------------------------------------------------------------------
	🔸 Generators are iterables - ex: range is an function generator
	🔸 Generators are functions that does not have any effect on the machine memory
		as it does not store in it but is handling iterations one by one by pausing 
		at each iteration
		- this is done using the `yield` keyword:
			it pauses the iteration process until specified not to ( using `next` )
			instead of returning a value stored in memory
		- `next(<generator>)`: gets the value depending on how many time next with the
		generator has been executed - it remembers the last value 
			- StopIteration Exception if next() is executed outside of the range 

-----------------------------------------------------------------------------------
''')
# Tooling
def try_catch(fn):
	def _(*args):
		try:
			fn(args[0])
		except:
			print( 'Impossible to process code')
	return 


print(f''' 
	Creation of "generator_function"
		- looping over a range
		- yielding an item instead of returning the item
''')
def generator_function(num):
	for i in range(num):
		print(f'yield i - : {i}')
		yield i 

print(f''' 
	Creation of a loop using the "generator_function"
		- looping over the iterable "generator_function"
		- printing the item : 💡 this is where it the item is
		 decided to be stored or else when generator functions
		 are used
''')
for item in generator_function( 10 ):
	print(f'item from generator processed: { item }\n')




generator_output = generator_function(10)
def get_index_in_range():
	try:
		output_generator_indexed_value = generator_function(10)[3]
		print( output_generator_indexed_value )
	except TypeError as error:
		print(f'''
		Impossible to execute this code:
			- Code: "output_generator_indexed_value = generator_function(10)[3]"
			- Error: {error}
		''')


# generator_output_indexed_value = generator_function(10)[3] # KO - TypeError:'generator' object is not subscriptable
print(f''' 
	🔸 Trying to :
		🔹 - store the value of a generator would return
			--> Result: {generator_output}

		🔹 - reach an item index of that range would return
			create an error ( it is an iterable but cannot return 
			a value not stored, just can create a process 
			that can pause along the executing process
			--> ❌ Error: 'generator' object is not subscriptable
			{get_index_in_range()}

		🔹 - `next([<generator>])` keyword allows to iterate manually over the
			generator in order to pause and get the value at a specific 
			iteration
			Executing x time next would tell the generator to reach xth value in
			the generator and keeps the very last value in memory
			--> first next executed: { next(generator_output) }
			--> second next executed: { next(generator_output) }
		)
''')


