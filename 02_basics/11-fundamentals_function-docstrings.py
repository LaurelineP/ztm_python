import os


################### DOCSTRINGS ###################
NEW_LINE = '\n\t'

# function definition and execution

print('\n\t---------------------------------------------------')
print(f'\t--------------  DOCSTRINGS  -------------')

definition = f'{ NEW_LINE }Docstrings are used to provide information regarding a function\'s usage' 
definition += f'{ NEW_LINE }To set a doctstring:'
definition += f'{ NEW_LINE } - write a pair of three single quotes within{ NEW_LINE }\tand right bellow the function definition statement'
definition += f'{ NEW_LINE } - inbetween this pair of opening and closing{ NEW_LINE }\tthree single quoted add a descriptive text'
definition += f'{ NEW_LINE } - accessing them would be while overing on the{ NEW_LINE }\t function execution or by printing it as follow:'
definition += f'{ NEW_LINE }\t\t --> "print( sayHello__doc__ )"'



print( definition )

print('\n\t---------------------------------------------------')


def sayHello():
  ''' Function saying hello'''
  print('hello')

print(f'\t\t DOCSTRING : "{sayHello.__doc__}"')
