# ---------------------------------------------------------------------------- #
#                  					SUPER()   	    	           	           #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
----------------------------------- SUPER() -----------------------------------
	The ability to pass from a inheriting class to its base class a new value 
	or to use the base class method / attribute
		- it can be done using `User.attack(self)`
			to refer to the parent class method
		- it can be done using `User.__init__(self, <attribute-to-update>)
			to update an unassign attribute inherited that is set to the class
			inheriting from the User class
		- it can be done using `super()` super().attack()
			to use the parent class method
		- it can be done using `super()` super().__init__.( email = <value> )
			to update the parent class attribute
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
		- result `player_email( wizard1 )`: {player_email( wizard1 )}
		- result `player_email( archer1 )`: {player_email( archer1 )}
            -----------------------------------------------
'''
)