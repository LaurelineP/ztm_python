'''
Objective: 
	- create a super list in a class SuperList
	- with a __len__ always equal to 1000
	- with every dunder method a list has
'''

class SuperList(list):
	def __len__(self):
		return 1000


my_list = SuperList()
print( len( my_list ))

my_list.append(5)
print(my_list[0])

print( issubclass( SuperList, list ))
print( issubclass( SuperList, object ))