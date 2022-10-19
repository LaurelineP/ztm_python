###################  FORMATTED STRING  ###################

# Helps in dynamically assign values to string without having
# to concatenate it with dynamical values
# - the string preceded by `f`, 
# - or using the `.format()` method at the end of the string, 
# will interpolate the curly braces by the values 
# accordingly to the order passed from the second argument to the last

print('FORMATTED STRINGS:\n A way to dynamically provide variables\'s value to a string \n by interpolating a curly braces \n ( and its content if any ) by the provided variables.')



# format() method and empty curly braces taking arguments order by default
print('\n1. FORMAT METHOD - ".format()" and empty curly braces ( since Python 2 )')
string_format1 = 'Hello {}, welcome to {}'.format('Lowla', 'Python')
_syntax_format1 = "Hello {}, welcome to {}'.format('Lowla', 'Python')"
print(" - Syntax:", _syntax_format1)
print(" - Result:", string_format1)

# format() method and curly braces with indexes taking arguments order by their indexes
print('\n\n2. FORMAT METHOD - ".format()" and curly braces \n\t with indexes ( since Python 2 )')
print('\tIndex following the order: 0, 1 ')
string_format2 = 'Hello {0}, welcome to {1}'.format('Lowla', 'Python')
_syntax_format2 = "Hello {0}, welcome to {1}'.format('Lowla', 'Python')"
print(" - Syntax:", _syntax_format2)
print(" - Result:", string_format2)



# format() method and curly braces with indexes taking arguments order by their indexes
print('\n\n3. FORMAT METHOD - ".format()" and curly braces with indexes at different places ( since Python 2 )')
print('\tIndex following the default order of the parameters: 0, 1 ')
string_format3 = 'Hello {1}, welcome to {0}'.format('Lowla', 'Python')
_syntax_format3 = "Hello {1}, welcome to {0}'.format('Lowla', 'Python')"
print(" - Syntax:", _syntax_format3)
print(" - Result:", string_format3)


# format() method and curly braces with indexes taking arguments order by their object names
print('\n\n4. FORMAT METHOD - ".format()" and curly braces with objects name ( since Python 2 )')

string_format4 = 'Hello {_name}, welcome to {_programming_language4}'.format(_name='Lowla', _programming_language4='Python')
_syntax_format4 = "Hello {name}, welcome to {programming_language}'.format(name='Lowla', programming_language='Python')"
print(" - Syntax:", _syntax_format4)
print(" - Result:", string_format4)




# `f` prepended to use it with variable ( Python 3 feature)
print('\n\n5. FORMAT METHOD - "f" ( only since Python 3 )')
_name = "Lowla"
_programming_language = "Pyton"
string_prepended_by_f = f'Hello {_name}, welcome to {_programming_language}'
_syntax_prepended_by_f = "f'Hello {name}, welcome to {programming_language}'"
print(" - Syntax:", _syntax_prepended_by_f)
print(" - Result:", string_prepended_by_f)