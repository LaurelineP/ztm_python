from time import time

print('''
		----------------------------------------------------------------------------
		-------------------------- GENERATORS PERFORMANCE --------------------------
		From prior written code : performance decorators, let's implement a generator instead
		- iterator
		- iterable

	
		''')

def get_performance( func ):
	def wrap_function( *args ):
		t1 = time()
		result = func( args )
		t2 = time()
		print(f'Took { args[0] } { t2 - t1 }s \n')

		return result
	return wrap_function

@get_performance
def process_time_consuming_code_from_generator( range_number = 0 ):
	print(f'[ GENERATOR ] Looping within a range of {range_number[0]} ...')
	for i in range(range_number[0]):
		i * 5


@get_performance
def process_time_consuming_code_from_list( range_number = 0 ):
	print(f'[ LIST ] Looping within a list of range of {range_number[0]} ...')
	for i in list(range(range_number[0])):
		i * 5

process_time_consuming_code_from_generator(100000000)
process_time_consuming_code_from_list(100000000)