# ---------------------------------------------------------------------------- #
#                		Functional programing  	           			      	   #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
			 Functional programing
-------------------------------------------------------------------------------
	2 RULES BOUND TO PURE FUNCTIONS: 
		🔸 For the same given inputs a function should always 
		   return the same return the same output
		🔸 A pure function should not have side effects
		  ( affecting elements ) outside its scope
''')
# Pure function
def pure_multiply( x, y ):
	return x * y

val1 = 2
val2 = 5
# Not pure function
def not_pure_multiply():
	return val1 * val2

# Pure function: returning a new object based on the init entry object
def pure_multiply_by2( list ):
	new_list = []
	for n in list:
		new_list.append(2 * n)
	return new_list


# Not pure function: returning a new object based on the init entry object
def pure_multiply_by2( list ):
	new_list = []
	for n in list:
		new_list.append(2 * n)
	return print( new_list ) # using print affect the outside scope


print(f'''
-------------------------------------------------------------------------------
				( code results )

	- [ PURE ] result of `pure_multiply` pure function: {pure_multiply(1, 5)}
		* this function relies only on the 2 given inputs to return a result

	- [ NOT PURE ]result of `not_pure_multiply` not pure function: {not_pure_multiply()}
		* this function relies on 2 given outer values to return a result

-------------------------------------------------------------------------------
				OBSERVATIONS

	🔸 Straight mutations to an outside object would be the result of a side effect
	🔸 Having the inputs as parameters and apply a logic to them returning a new object
		will - all being contained - would represent a pure function

	With pure functions the code tends to have less buggy behaviors
	Pure function is more of a guideline than an absolute rule
	but whenever a dev can, she/he should implement pure functions
''')

print('''
-------------------------------------------------------------------------------
			OOP INTO FP

	In OOP, we've made a Wizard class ( mixing both data and methods 
	related to the same object )
	Let's interpret it as FP and see how is it:

	```python
	# ------------ OOP Way
	class Wizard:
		def __init__(self, name, power ):
			self.name = name
			self.power = power

		def attack( self ):
			return f'{{ self.name }} attacks with {{ self.power }}'

	# ------------ FP Way
	# data dissociated
	wizard = {
		"name": 'Merlin',
		"power": 'Magical powers',
	}

	# function dissociated
	def attack( character ):
		return f'{{ character["name"] }} attacks with {{ character["power"] }}'
	```

''')

# ------------ OOP Way
class Wizard:
	def __init__(self, name, power ):
		self.name = name
		self.power = power

	def attack( self ):
		return f'{ self.name } attacks with {self.power}'

print( Wizard( 'Merlin', 'magical powers').attack())


# ------------ FP Way
# data dissociated
wizard = {
	"name": 'Merlin',
	"power": 'Magical powers',
}

# function dissociated
def attack( character ):
	return f'{ character["name"] } attacks with {character["power"] }'

print( attack( wizard ))