# ---------------------------------------------------------------------------- #
#                  				MULTIPLE INHERITANCE  	           	      	   #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
			 MULTIPLE INHERITANCE 
-------------------------------------------------------------------------------
	Multiple inheritance allows to inherit from different object
	This is powerful however it will get complexioned in order to pass
	the rights parameters according to each object constructor
		- had to pass num_arrows to Archer object constructor to enable HibridBorg
		to state the arrows number in its attack
		- had to override attack to benefits both Wizard and Archer attacks ( extra )

		---------------------------------------------------
		( python code )

		...
		def __init__(self, name, power, num_arrows):
			Archer.__init__(self, name, num_arrows )
		Wizard.__init__(self,	name, power)

		def attack(self):
			wizard_attack = Wizard.attack(self)
			archer_attack = Archer.attack(self)
			return f'{{wizard_attack}}{{archer_attack}}'
		----------------------------------------------------

''')
class User:
	def sign_in( self ):
		return 'Logged in'
	
	def attack( self ):
		print('Does nothing')

class Wizard(User):
	def __init__(self, name, power):

		self.name = name
		self.power = power
	
	def attack(self):
		return f'Attacking with the power of {self.power}'


class Archer(User):
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows or 0
	
	def attack(self):
		super().attack()
		return f'Attacking with the arrows; arrows left: {self.num_arrows}'
	
	def get_arrows_quantity(self):
		return self.num_arrows

	def run(self):
		return 'Run for your life !!!'

# HybridBorg has inherit from both wizard and Archer
class HybridBorg(Wizard, Archer):
	# as wizard got instantiated first and the second parameters of wizard is power not arrows
	# we will need to spawn parent classes and customise how HybridBorg gets initiated
	def __init__(self, name, power, num_arrows):
		Archer.__init__(self, name, num_arrows )
		Wizard.__init__(self,	name, power)

	def attack(self):
		wizard_attack = Wizard.attack(self)
		archer_attack = Archer.attack(self)
		return f'{wizard_attack}\n{archer_attack}'


wizard1 = Wizard('Merlin', 'wind')
archer1 = Archer('Archibald', 40)
hybrid1 = HybridBorg('TitanBorg', 'strength', 100 )

# Using classes polymorphism
def player_attack( character ):
	return character.attack()

def player_email( character ):
	return character.email

print( hybrid1.run() )
print( hybrid1.get_arrows_quantity())
print( hybrid1.attack())