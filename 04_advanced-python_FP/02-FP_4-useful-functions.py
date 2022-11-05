# ---------------------------------------------------------------------------- #
#                		   4 USEFUL FUNCTIONS  	           			      	   #
#                  - map(), filter(), zip(), reduce() - 	           		   #
# ---------------------------------------------------------------------------- #
from functools import reduce


print('''
-------------------------------------------------------------------------------
			 4 USEFUL FUNCTIONS
		 - map(), filter(), zip(), reduce() - 
-------------------------------------------------------------------------------
	These built-in functions are commonly use while coding in Python
''')

# Regular loop approach
def multiply_by2_classic( list ):
	print( list )
	new_list = []
	for n in list:
		new_list.append( n * 2 )
	return new_list

print('''
-------------------------------------------------------------------------------
			 Built-in function `map()`

	🔸 Purpose: looping and process something within an iterable 
	🔸 Syntax: map(<function>, <*iterables> )
	 - Example: map( multiply, [1,2,3])
	🔸 Explanation: 
	 	map() will loop over the iterable,
		taking each item from the iterable and
	 	call the function for each iteration
	It always returns an object with the same initial object length

	🔸 Returns: a NEW "map object" ( ex: "<map object at 0x105e89210>" )
		without mutating the initial iterable object


	🔸 Tip: read the returned value of the function "map()"
		using the "list()" function
		Ex: list( map(multiply_by2_map, [6,7,8] ) )
	
''')
# 
def multiply_by2_map( n ): return n * 2

# Note: highlight the functional programing paradigm :
#       - separate functions and data
result = map(multiply_by2_map, [6,7,8] )
print( f'		- Result map with inline iterable: { list(result) }\n')


# Using map() with data in outer scope
my_list = [1,2,3]
result = map(multiply_by2_map, my_list )
print(f'		---> initial iterable { my_list }')
print(f'		- Result map with outside iterable: {  list(result) }')
print(f'		---> initial iterable did not change: { my_list }')



print('''
-------------------------------------------------------------------------------
			 Built-in function `filter()`

	🔸 Purpose: filtering within an iterable 
	🔸 Syntax: filter(<function>, <*iterables> )
	 - Example: filter( get_odd, [1,2,3])
	🔸 Explanation: 
	 	filter() will loop over the iterable,
		evaluating each item from the iterable and
	 	will return if the function called against
		the iterable returns True
	It can returns an object with less than the object length
	

	🔸 Returns: a NEW "filter object" ( ex: "<filter object at 0x105e89210>" )
		without mutating the initial iterable object


	🔸 Tip: read the returned value of the function "map()"
		using the "list()" function
		Ex: list( filter(get_odd, [6,7,8] ) )
	
''')
# 
def get_odd( n ): return n % 2 == 1

# Note: highlight the functional programing paradigm :
#       - separate functions and data
result = filter(get_odd, [6,7,8] )
print( f'		- Result filter: { list(result) }\n')


print('''
-------------------------------------------------------------------------------
			 Built-in function `zip()`

	🔸 Purpose: combine iterables into one iterable -> each item of both 
		list will be grouped by their index into a tuple
	🔸 Syntax: zip(<*iterables>, ...)
	 - Example: zip([1,2,3], [4,5,6])
	 Explanation: 
	 	zip() will loop over the iterables simultaneously-like,
		taking each item from each iterable and
	 	gather each item at same index for all list together into
		a tuple

	🔸 Returns: a NEW "zip object" ( ex: "<reduce object at 0x105e89210>" )
		without mutating the initial iterable object

	🔸 Tip: read the returned value of the function "map()"
		using the "list()" function
		Ex: list( zip( [1,2,3], [4,5,6] ) )
	
''')
# Note: highlight the functional programing paradigm :
#       - separate functions and data
result = zip(['six', 'seven', 'height'],[6,7,8] )
print(f'		Code: "zip(["six", "seven", "height"] [6,7,8] )')
print( f'		- Result: { list(result) }\n')






print('''
-------------------------------------------------------------------------------
			 Built-in function `reduce()`

	📌 Reduce is not a built in function however it comes from a built-in module
		that needs to be imported
	🔸 Purpose: reducing an into one value 
	🔸 Syntax: reduce(<function>, <*iterables>, <initialValue> )
	 - Example: reduce( sum, [1,2,3], 0)
	 Explanation: 
	 	reduce() will loop over the iterable,
		taking the initial value and each item from the iterable and
	 	will execute the given function passing those 2 arguments
		in order to apply a process on both of them.
		The (updated) returned value will be given through
		all iteration to repeat the process

	🔸 Returns: a NEW "reduce object" ( ex: "<reduce object at 0x105e89210>" )
		without mutating the initial iterable object


	🔸 Tip: read the returned value of the function "map()"
		using the "list()" function
		Ex: reduce(sum, [6,7,8], 0 ) )
	
''')
# 
def sum( init, n ): 
	return init + n

# Note: highlight the functional programing paradigm :
#       - separate functions and data
result = reduce(sum, [6,7,8], 0 )
print( f'		- Result: { result }\n')
