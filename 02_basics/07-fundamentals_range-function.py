################### RANGE ###################

print(f'\n\t--------------------- RANGE: ---------------------')

# Range
description = f'\n\tA range has a start and end points to constitute a range of values'
description = description + f'\n\n\t 🔸 Tip : Quite useful when dealing with list to create or for iterations'
description = description + f'\n\t 🔸 Syntax: `range(<number>[<number>[<jumping-step-number( reversed or not)>]])`'

# A range
range10 = range(10)
description = description + f'\n\n\t\t - `range(10)` or `range(0, 10)` would give a descending --> {range10}'
print( description )

print('\n\t---------------------------------------------------')


# [ Use case ] Looping over a descending range
print(f'\n\t LOOPING OVER A DESCENDING RANGE:')
for number in range10:
  print(f'\n\t - range iteration: {number}')
  

# [ Use case ] Looping over an ascending range ( reversed order )
print(f'\n\n\t LOOPING OVER AN ASCENDING RANGE:')
range10_reversed = range(10 ,0, -1)
for number in range10_reversed:
  print(f'\n\t - range iteration: {number}')


# [ Use case ] Looping over an ascending range ( reversed order )
print(f'\n\n\t CREATE LIST WITH RANGE:')
list_with_range = list(range(10))
print(f'\n\t - list of range: {list_with_range}')
  