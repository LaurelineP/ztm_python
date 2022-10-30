# ---------------------------------------------------------------------------- #
#                  				INTROSPECTION AND  	             	      	   #
# 									DUNDER METHODS   	             	       #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
			 INTROSPECTION AND 
				DUNDER METHODS 
-------------------------------------------------------------------------------

	🔸 INTROSPECTION ---------------------------------------------------
		We can introspect an object by using `dir(<instance>) built-in function`
		This will list all attributes / methods from an object

''')
class User:
	''' 1a. preparing potential class attributes coming from sub classed setting them'''
	def __init__(self, email):
		self.email = email

	def sign_in( self ):
		return 'Logged in'
	
	def attack( self ):
		print('Does nothing')

class Wizard(User):
	def __init__(self, name, power, email):
		'''1b. hack way'''
		# User.__init__(self, email = email )

		'''1c. super way'''
		super().__init__(email)
		self.name = name
		self.power = power
	
	def attack(self):
		return f'Attacking with the power of {self.power}'


class Archer(User):
	def __init__(self, name, num_arrows, email):
		'''1b. hack way'''
		# User.__init__(self, email = email )

		'''1c. super way'''
		super().__init__(email)
		self.name = name
		self.num_arrows = num_arrows or 0
	
	def attack(self):
		''' 0a. quick hack calling the "parent" class'''
		# User.attack(self)
		''' 0b. how it's done today '''
		super().attack()
		return f'Attacking with the arrows; arrows left: {self.num_arrows}'

wizard1 = Wizard('Merlin', 'wind', 'merlin@mail.com')
archer1 = Archer('Archibald', 40, 'archibald@mail.com')

# Using classes polymorphism
def player_attack( character ):
	return character.attack()

def player_email( character ):
	return character.email

print(f'''
		- introspecting wizard `dir( wizard1 )`: \n\n\t{dir( wizard1 )}\n\n
            -----------------------------------------------
'''
)



print('''

	🔸 DUNDER METHODS ---------------------------------------------------
		https://docs.python.org/3/reference/datamodel.html#special-method-names
		exo: https://repl.it/@aneagoie/Dunder-Methods
		
		Description: Dunder methods are methods that start and end with double underscore
		`__init__()` if a dunder method

		Overriding dunder methods in general should be avoided however sometimes it 
		may be useful in some cases when you want an object to behave a certain way:
		Example : str of a class will return the object location when maybe we want
		a specific information instead of thE __main__<xxxxxxxx>
		This allows to customized the object we are defining

''')

class Toy():
	def __init__(self, color, age = 0):
		self.color = color
		self.age = age
		self.items = {
			'name': 'Yoyo',
			'age': self.age,
		}

	""" overriding __str__ by changing its regular behavior
		which is to return --> "<__main__.Toy object at 0x101c351b0>"
	"""
	def __str__(self):
		return self.color

	""" overriding __len__ by changing its regular behavior
		which is crashing the code with an error 
		--> "object of type 'Toy' has no len()" 
	"""
	def __len__(self):
		return 5

	
	""" overriding __del__ by changing its regular behavior
		which is deleting the item 
	"""
	def __del__(self):
		print('deleted!')



	""" overriding __call__ : by defining it we make the object callable
		with parentheses ( ex: myToy()) ( parentheses here at the end represent __call__
	"""
	def __call__(self):
		return("🤙 yesss!")


	""" overriding __call__ : by defining it we make the object callable
		with parentheses ( ex: myToy()) ( parentheses here at the end represent __call__
	"""
	def __getitem__(self, key):
		return self.items[key]


myToy = Toy("red")

print(f'''
	- myToy listed with dir built-in function: {dir(myToy)}
	
	- myToy listed with dir dunder method: {myToy.__dir__()}
	
	Both result output the same values ( here in different order though )
''')

print(f'''
	After overriding some dunder methods
	- "str" overridden : "{str(myToy)}" instead of "<__main__.Toy object at 0x101c351b0>"
	- "len" overridden : "{len(myToy)}" instead of "object of type 'Toy' has no len()"
	- "del" overridden : "del myToy" : will print "deleted!" instead of deleting an item
	- "call" overridden :{myToy.__call__()} : instead of "'Toy' object has no attribute '__call__'"
		- can also be written : myToy()
		- can also be written : myToy.__call__()
	- "getitem" overridden :{myToy.__getitem__('name')} : instead of "''Toy' object has no attribute '__getitem__'"
		- can also be written : myToy.__getitem__('name')
		- can also be written : myToy['name']
''')
