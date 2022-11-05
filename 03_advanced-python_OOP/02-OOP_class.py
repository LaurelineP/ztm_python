# ---------------------------------------------------------------------------- #
#                  CREATING CUSTOM OBJECTS ( CLASS )                           #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
------------------- CREATING CUSTOM OBJECTS ( CLASS )-------------------------
    🔸 Custom objects are blueprint for instances
	- as a blueprint: the naming convention is 
	to use singular word

    🔸 Creating a class object
	- declare the object with `class`
	- define the object name starting with a capital
	- define the object name is camelCase

	- [ optional ] first function must me an `__init__(self, name):`
	( 2 underscores are called dunder or magic method )
		- self refers to itself, ( the caller instance )
		parameters after would be attributed

	- Instances are create from the same class object 
	but printing those will create another object into memory
	( which is what we want ) --> instantiating

            -----------------------------------------------

'''
)

class Player:
    # class object attributes
    '''
     - static attributes are regular variables
     - accessed as follow: <CLASS>.<STATIC-ATTRIBUTE>
     '''
    membership = True

    # "init" or "constructor" method
    def __init__(self, name):
        # dynamic attributes starts with self
        self.name = name

    def run():
        print('run')

    def shout(self):
        nameFormatted = self.name.upper()
        print(f'MY NAME IS { nameFormatted }')

    def get_full_description(self, extra):
        print(f'My name is { self.name } and I can')
        if (extra):
            print(f'I also like {extra}')

    # adding decorators

    # - useable without having to instantiate a class
    @classmethod
    def adding_things( cls, num1, num2 ):
        return num1 + num2

    @staticmethod
    def get_personal_message( msg ):
        return msg



print(f'''
-------------------------- INSTANTIATING --------------------------------

        All instances will benefits of everything defined
        within the class
        - application:
            "player1 = Player('Lowla')"
            "player1.shout()"


        Printed answers:
''')
# instantiating Player as players
player1 = Player("Lowla")
player1.shout()
# player1.shout('ROCK') # TypeError: shout() takes 1 positional argument but 2 were given

player1.get_full_description('learning, coding')

print(f'''
    - returns: { player1.shout() }
    - returns: { player1.get_full_description('learning') }

            -----------------------------------------------



''')



5

print(f"""
-------------------------------- DECORATORS --------------------------------------

    Adding decorators
    When to use what : https://www.makeuseof.com/tag/python-instance-static-class-methods/
    🔸 @classmethod( cls, <args>...)
        - useable without instantiating a class 
        by doing the following "Player.adding_things('x', 'y')"
        - ability to use the class itself through "cls('PlayBoy')"
        --> result: { Player.adding_things('x', 'y') }


    🔸 @staticmethod
        - useable ONLY on instances ( private to that instance )
        by doing the following "player1.get_personal_message('Hello World')"
        --> result: { player1.get_personal_message('Hello World') }

""")
result = player1.adding_things('hello ', 'world')
print('\tresult:', result)