#OOP 
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

# ---------------------------------------------------------------------------- #
#                             CREATE OWN DATA TYPE                             #
# ---------------------------------------------------------------------------- #
# Using the keyword `class`
# 		- Classes start with a capital
# 		- Classes are written in camelCase
class BigObject:
	pass

object1 = BigObject # this is an instance

print(type(BigObject)) # <class 'type'>
print(type(object1)) # <class '__main__.BugObject'>

