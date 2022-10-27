################### GLOBAL KEYWORD ###################
print(f'\n\t------------------- GLOBAL KEYWORD -------------------')
NEW_LINE = '\n\t'

# Description
description = f"{ NEW_LINE } When changing scope ( e.g.: function )"
description += f"{ NEW_LINE } sometime we want to use a variable in the global scope"
description += f"\n{ NEW_LINE } To do so, we must use `global` keyword, within the function,"
description += f"{ NEW_LINE } to assign a local variable refering to a global variable"
description += f"{ NEW_LINE } ( *this will affect the global variable value )"

print( description )

print('\n\t------------------------------------------------')

total = 0

def count():
  global total
  total += 1
  return total

# dynamically count x times
while( total < 3): count()
print(total)

# manually count x times: another way to do with passing an argument
total = 0
def count_arg(total):
  total += 1
  return total

# when not re-assigning the global variable, this one remains unchanged
print(f'{ NEW_LINE } - when not re-assigning the global variable, this one remains unchanged')
print('\t\t Output in print: ', count_arg(count_arg(count_arg(total))) )
print( f'\t\t Result printing global total: { total } ')

# when re-assigning the global variable, this one changes
print(f'{ NEW_LINE } - when re-assigning the global variable, this one changes')
print('\t\t Output in print: ', count_arg(count_arg(count_arg(total))) )
total = count_arg(count_arg(count_arg(total)))
print( f'\t\t Result printing global total: { total } ')
