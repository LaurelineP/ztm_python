# ---------------------------------------------------------------------------- #
#                  				4 PILLARS OF OOP   	             	           #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
---------------------------- 4 PILLARS OF OOP ---------------------------------


🔸 ENCAPSULATION --------------------------------------------------------------
	It's a binding of data within functions that manipulates that data.
	Those data within and functions are what is called attributes and methods
	A class without any functions ( just the attributes ) is useless as it only serve 
	to store the data like a dictionary would

	🔹 The only differences are:
		- how those 2 kind of objects are accessed
			- class: with squared bracket notation
			- dict: with dot notation

            -----------------------------------------------
''')
NEW_LINE = '\t\t'
class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Bracket notation accessing attribute "name" 's value
player_class = Player('Majo', 1000 )
print(f'{ NEW_LINE } - Player Class name: {player_class.name}')

# Dot notation accessing key "name" 's value
player_dict = { "name": "Majo", "age": 1000 }
print(f'{ NEW_LINE } - Player Dictionary name: {player_dict["name"]}')



print('''



🔸 ABSTRACTION:  --------------------------------------------------------------
	Hiding away information and giving access to the only things needed 
	We can see abstraction in any code we write: object possesses a lot of
	attributes and functionalities without thinking of how it is implemented

	Those correlate here to private and public variable
		Class can me overridden when assigning a new value to the public variable
		🔹 In python there are no real privacy ( and no private keyword ) but
			we can specify it by having an _ ( underscore before the variable ) as
			this represent a convention to express the privacy


            -----------------------------------------------

'''
)

print('''



🔸 Inheritance:  --------------------------------------------------------------
	An object taking the properties of another object: this is inheritance
	Note: a class is not necessarily defined with a dunder method ( __init__ ) when
	a class does not have any attributes for instance
	Inheritance is useful when you want to assign a new object with those attributes or
	method : it extends the proprieties of another object if assigned to another one

		🔹 To do so:
			- while defining a class add parentheses with the the class
			to inherit from :
		------------------------------------
			class User:
				# no __init__
					def sign_in( self ):
						print(' logged in ')

			class Wizard( User ):
				pass

			- checking if Wizard did inherit from User
			print( Wizard.sing_in())
		-------------------------------------
'''
)
class User:
	# no __init__
	def sign_in( self ):
		return 'Logged in'
	
	def attack( self ):
		return 'Does nothing'

class Wizard(User):
	def __init__(self, name = 'Mysterious', power='unknown powers'):
		self.name = name
		self.power = power
	
	def attack(self):
		return f'Attacking with the power of {self.power}'


class Archer(User):
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows or 0
	
	def attack(self):
		return f'Attacking with the arrows; arrows left: {self.num_arrows}'

wizard1 = Wizard('Merlin', 'all mighty powers')
archer1 = Archer('Robin', 100)

wizard_sign_in = wizard1.sign_in()
wizard_attack = wizard1.attack()

print(f""" 	\t\t- Result sign-in method: {wizard_sign_in}
			- Result attack method: {wizard_attack}
""")

print(f'''

🔹 Checking if an object is an instance of another onw with 'isinstance':
			- syntax: `isinstance( <instance>, <class-to-check>)`
			- example: `isinstance( wizard1, User )`
			- example: `isinstance( wizard1, object )` ( base class )
			- result: {isinstance( wizard1, User )}
			- result: {isinstance( wizard1, object )} ( base class )
			- result: {isinstance( wizard1, User )}
''')



print('''



🔸 POLYMORPHISM:  --------------------------------------------------------------
	Poly ( many ), morph ( shape )
	Polymorphism in Python refers to the way classes can share the same method name.
	Those method name can be accessed differently based on what object calls it
	The ability to redefine method ( from inherited method in the other class )

	Example Wizard and Archer have the same callable method but those are different
	from each other / representing two different needs for each class


            -----------------------------------------------

'''
)

print('''
	🔹 This could be depict by creating a function receiving one object and having that
	function executing the same method name for any object passed
	Code: `def player_attack( character ): character.attack()`
	( This approach could be used within a loop )
'''
)

def player_attack( character ):
	return character.attack()

print(f'''
		- result `player_attack( wizard1 )`: {player_attack( wizard1 )}
		- result `player_attack( archer1 )`: {player_attack( archer1 )}
            -----------------------------------------------
'''
)