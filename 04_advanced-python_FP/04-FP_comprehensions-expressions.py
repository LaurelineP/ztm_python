# ---------------------------------------------------------------------------- #
#                		   COMPREHENSIONS	            			      	   #
# ---------------------------------------------------------------------------- #
from functools import reduce



def display_introduction():
	print('''
	-------------------------------------------------------------------------------
				COMPREHENSIONS
	-------------------------------------------------------------------------------
		🔸 This is used for the following iterable dataTypes
			- list
			- set
			- dictionary
		🔸 Expressions shorthand enabling to go though an iterable to build
			a list with each value
		🔸 Pro and Cons:
			- 👍 prevents on relying on loop block scope to do the same
			- 👎 the more complex the comprehensions is,
				the most it decreases the code readability
	''')


def display_list_comprehension():
	print('''
	-------------------------------------------------------------------------------
				LIST COMPREHENSION
		🔸 Syntaxes: 
			0 - get every item from an iterable
				[<param> for <param> in <iterable>]
			
			1 - apply operation on each item from an iterable
				[<operation-with-param> for <param> in <iterable>]
		
			2 - filter item from iterable meeting condition
				[<param> for <param> in <iterable> if <condition>]
			
			3 - apply operation on kept item from iterable meeting condition
				[<operation-with-param> for <param> in <iterable> if <condition>]
			
	''')
	sentence = 'Hello World'
	numbers = [ 67, 34, 53, 78 ]
	# 0. Most classing way to create a list from an iterable
	characters_from_loop = []
	for character in sentence:
		characters_from_loop.append( character )

	# 1. The above could be done with list comprehension expression
	characters_comprehension = [ character for character in sentence ]


	# 2. List comprehension with operation to apply to each item
	characters_upper_comprehension = [ character.upper() for character in sentence ]


	# 3. List comprehension with operation to apply to each item if/for the value is meeting the condition
	numbers_even = [ n for n in numbers if n%2 == 0 ]

	# 4. List comprehension with operation to apply to each item if/for the value is meeting the condition
	numbers_with_some_divided = [ n/2 for n in numbers if n%2 == 0 ]


	print( f'''
		---------------------------------------------------------
		Code results
		1. Result using classic list comprehension:
			--> {characters_comprehension}''' )


	print( f'''
		2. Result using list comprehension with an operation
		to apply to each item:
			--> {characters_upper_comprehension}''' )

	print( f'''
		3. Result using list comprehension to keep item if item
		meets the condition - acting like filter
			--> {numbers_even}''' )

	print( f'''
		4. Result using list comprehension to keep and change the item if item
		meets the condition - acting like filter
			--> {numbers_with_some_divided}''' )


def display_set_and_dictionary_comprehensions():
	print('''
	-------------------------------------------------------------------------------
				SET / DICTIONARY COMPREHENSION
		Reminder: set is a dataType returning unique value ( any duplicates does not exist within )
		🔸 Syntaxes: 

			0 - set comprehension: 
				{ <keyParam > for <keyParam> in <iterable> }

			1 - dictionary comprehension: 
				<keyParam : valueParam> for <keyParam , valueParam> in <same-iterable> }

				{ <keyParam : keyParam> for <keyParam> in <diff-iterable-with-no-key-value-pair> }

			2 - apply operation on each item from an iterable
				{ <keyParam : valueParam> for <keyParam , valueParam> in <same-iterable> }
		
			3 - filter item from iterable meeting condition
				{ <keyParam : valueParam> for <keyParam : valueParam> in <iterable> if <condition>}
			
			4 - apply operation on kept key/value pairs from iterable meeting condition
				{<keyParam : valueParam operation(s)> for <keyParam : valueParam> in <iterable> if <condition>}
			
	''')


	sentence = 'Hello World'
	dictionary = { 'name': 'Smith' }

	# 1. Set comprehension : will create a set data structure with unique items
	my_set = { character for character in sentence }


	# 2. Dictionary comprehension from another dictionary
	my_dict = { key:value for key,value in dictionary.items() }


	# 3. Dictionary comprehension with operation to apply to each key and value pair of another dictionary
	my_dict_mutated= { key.upper():value.upper() for key,value in dictionary.items() }

	# 4. List comprehension with operation to apply to each item if/for the value is meeting the condition
	my_dict_from_list = { num: num*2 for num in [1,2,3,4,5,6] }


	# 5. List comprehension with operation to apply to each item if/for the value is meeting the condition
	my_dict_from_list = { num: num*2 for num in [1,2,3,4,5,6] }

	print( f'''
		---------------------------------------------------------
		Code results
		1. Result using classic set comprehension:
			--> {my_set}''' )


	print( f'''
		2. Result using classic dictionary comprehension:
			--> {my_dict}''' )


	print( f'''
		3. Result using classic dictionary comprehension applying a change 
			--> {my_dict_mutated}''' )


	print( f'''
		4. Result using list comprehension to build an dictionary from a list
			--> {my_dict_from_list}''' )




display_introduction()
display_list_comprehension()
display_set_and_dictionary_comprehensions()