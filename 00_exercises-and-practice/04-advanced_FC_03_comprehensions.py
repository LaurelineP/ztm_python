print('''
—--------------—--------------—--------------—--------------—--------------—--------------
	Objective: 
		From the bellow code checking classically duplicates,
		use comprehensions to do the same instead of relying on 
		a loop block

	—--------------—--------------—--------------—--------------
''')

letters = ['a', 'b', 'c', 'd', 'e', 'd', 'a', 'n', 'm', 'n']
duplicates = []

# Given code example
non_duplicates = []
for l in letters:
    if l not in non_duplicates:
        non_duplicates.append(l)
    else:
        duplicates.append(l)


# Code using comprehension
duplicates_comprehension = list({l for l in letters if letters.count(l) > 1})

print(f'''
		Duplicates found using comprehensions: { duplicates_comprehension }
		- Personal approach: 
			--> list({{l for l in letters if letters.count(l) > 1}})
		- Solution/correction from course:
			--> list(set([x for x in some_list if some_list.count(x) > 1]))
			link: https://replit.com/@aneagoie/comprehension-1#main.py

			
''')
