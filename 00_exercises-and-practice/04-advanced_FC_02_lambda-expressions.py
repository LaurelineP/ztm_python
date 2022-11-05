'''
Objective: 
	practice lambda expressions
'''
from cmath import sqrt


numbers = [ 39,56,67,345,13,762,65,3 ]
result = map( lambda n: n * n, numbers)
print(f'''
	🔸 I: Create a lambda expression that squares numbers in a list
	   - Map and square result:
		--> original list: { numbers }
		--> result list: { list(result) }
''')

sorting_list = [(0,2), (4,3), (9,9), (10,-1)]
result = sorted( map(lambda tuple: tuple[1], sorting_list))
sorting_list.sort(key=lambda tuple: tuple[1])
course_solution = sorting_list
print(f'''
	🔸 I: Create a lambda expression that help to sort the list of tuples 
		by its second item ( item[1] )
	   - Sort by second placed item within tuple:
		--> original list: { sorting_list }
		--> result list: { list(result) }
		--> result course solution: { list(sorting_list) }
''')
