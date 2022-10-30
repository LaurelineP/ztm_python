################### FOR LOOP ###################

print(f'\n\t--------------------- ITERABLES: ---------------------')

# For loop description
description = f'\n\tAllows to run a code over and over'
description = description + f'\n\t - Syntax: "for <item-variable> in <iterable: list | tuples | Sets >"'
description = description + f'\n\t - Example: "for caracter in "Hello worlds""'
print( description )

print('\n\t---------------------------------------------------')


# For loop in application

objective = input('\n\t What is your goal? ')
for character in objective:
  if character == " ":
    print('\n')
  else:
    print(f'\t "- character" is :{character}')
  
