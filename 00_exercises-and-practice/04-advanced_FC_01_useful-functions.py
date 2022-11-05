'''
Objective: 
	Practice the use of those 4 commonly used function in python 
	( map(), filter(), zip(), reduce() )
'''

from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item): return f'{ item.capitalize() }'


result = list(map(capitalize, my_pets))
print(f'- Capitalized items: {result}')


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
result = list(zip(my_strings, my_numbers))
print(f'- Zipped items: {result}')


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def is_over_50(n): return n >= 50


result = list(filter(is_over_50, scores))
print(f'- Filtered items over 50: {result}')


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(init, n): return init + n


new_list = my_numbers[:]
new_list.extend(scores)
result = reduce(accumulate, new_list, 0)
print(f'- Reduced numbers into one total of: {result}')
print(f'Course solution: https://replit.com/@aneagoie/functional#main.py')
