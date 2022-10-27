################### FUNCTIONS AND *ARGS AND *KWARG ###################
NEW_LINE = '\n\t'

# function definition and execution

print('\n\t---------------------------------------------------')
print(f'\t-------  FUNCTIONS AND *ARGS AND *KWARGS  --------')

definition = f'{ NEW_LINE }Back to the function arguments' 
definition += f'{ NEW_LINE }If you want to get arguments without knowing them,'
definition += f'{ NEW_LINE }a generic way to catch them is to use'
definition += f'{ NEW_LINE }`*args` and/or `**kwargs`.'

definition += f'\n{ NEW_LINE } 🔸 Rules: ( value1, *args, word = "WORD", **kwargs )'
definition += f'\n{ NEW_LINE }\t - *args: represent a bunch of parameters that'
definition += f'{ NEW_LINE }\t\tdo not have keywords - a tuples of values is returned'
definition += f'\n{ NEW_LINE }\t - **kwargs: represent a bunch of parameters that'
definition += f'{ NEW_LINE }\t\tdo not have keywords - a dictionaries is returned'
definition += f'\n{ NEW_LINE } 🔸 Syntax: "def say_custom hello(name, *args, emoji = "👋", **kwargs)""'
definition += f'\n{ NEW_LINE }\t ▶️ Executing: { NEW_LINE }\t\t"sayHello({ NEW_LINE }\t\t\t\'L O W L A\',{ NEW_LINE }\t\t\t 1,2,3, { NEW_LINE }\t\t\t emoji = \'👺\',{ NEW_LINE }\t\t\t age = \'unknown\',{ NEW_LINE }\t\t\t country= \'France\'{ NEW_LINE }\t\t)"'
print( definition )

print('\n\t---------------------------------------------------')

def sayHello(name, *args, emoji = "👋", **kwargs):
  _args = args
  _kwargs = args
  print(f'{ NEW_LINE }Within the function printing args and kwargs:')
  print(f'{ NEW_LINE }\t\t - extra args are: {args}')
  print(f'{ NEW_LINE }\t\t - extra kwargs are: {kwargs}')
  return (f'Hello { name } { emoji } !')

result = sayHello('L O W L A', 1,2,3, emoji = '👺', age = 'unknown', country= 'France')

print(f'{ NEW_LINE }Example:')
print(f'{ NEW_LINE }Result: \t\t{ result }')
