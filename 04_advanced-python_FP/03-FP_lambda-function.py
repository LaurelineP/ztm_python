# ---------------------------------------------------------------------------- #
#                		   LAMBDA FUNCTION	            			      	   #
# ---------------------------------------------------------------------------- #
from functools import reduce


print('''
-------------------------------------------------------------------------------
			 LAMBDA FUNCTION
-------------------------------------------------------------------------------
	🔸 Anonymous function used once 
		Example: function to provide to: map(), filter(), reduce()
	🔸 Syntax: lambda <parameter-name>: <code-applied-to-param>
''')
numbers = [ 2,4,56,7,3,12,54,82,23 ]
numbers_by_2 = map( lambda n: n * 2, numbers)
print(f'''Result using lambda "map( lambda n: n * 2 )":
	- original list: {numbers}
	- result {list(numbers_by_2)}''')

filtered_even = filter( lambda n: n % 2 == 0, numbers )
print(f'''Result using lambda "filter(lambda n: n % 2 == 0, numbers )":
	- original list: {numbers}
	- result {list(filtered_even)}''')