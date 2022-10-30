################### SCOPES ###################
print('\n\t------------------------------------------------')
print(f'\t-------------------  SCOPES -------------------')
NEW_LINE = '\n\t'

# Description
description = f"{ NEW_LINE } Scope represents a block of code relative to the line executed { NEW_LINE } and what is able to be reached"
description += f"{ NEW_LINE } Or which variable is accessed"
description += f"{ NEW_LINE } It could be local / function scope or global"

print( description )

print('\n\t\t\t----------------------------')

var = 0
def reassign_variable():
  var = 5
  return var
  

reassign_variable()
print(f'{ NEW_LINE } Example:')
print(f'\t - [ global scope ] var init is: ', var)
print(f'\t - [ function scope ] var in function is:', reassign_variable())
print(f'\t - [ global scope ] var after function execution is:', var)

conclusion = f'\n{ NEW_LINE } Finally: each time a function is created { NEW_LINE } we can see it creates a new whole scope'

print( conclusion )

print('\n\n\t------------------------------------------------')
print(f'\t----------------- SCOPES RULES -----------------')
description = f'{ NEW_LINE } Scopes rely on rules ( order of scope to accessed )'
description += f'{ NEW_LINE }\t 📜 Rule 1: start with local scope variables'
description += f'{ NEW_LINE }\t 📜 Rule 2: search for higher scope ( before this current scope )'
description += f'{ NEW_LINE }\t 📜 Rule 3: if no higher scope defined, it accesses the global scope'
description += f'{ NEW_LINE }\t 📜 Rule 4: if not defined in global scope, search for python functions{ NEW_LINE }\t\t( build-in variables )'
print( description )
