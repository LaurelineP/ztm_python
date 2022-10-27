################### ENUMERATE ###################

print(f'\n\t--------------------- ENUMERATE: ---------------------')

# Enumerate
description = f'\n\tAn enumerate function outputs the interfacing between an iterable index and the value at this index'

description = description + f'\n\n\t 🔸 Syntax: `enumerate(<iterable>)`'

# Enumerate use
enumerate_range_10 = enumerate(range(50,60))
description = description + f'\n\t\t - `enumerate(range(10))` would give an enumeration of each item \n\t\t\treturns --> {enumerate_range_10}'

description = description + f'\n\n\t 🔸 Tip : Quite useful when dealing with iterations ( --> loops related )'

print( description )

print('\n\t---------------------------------------------------')


# # [ Use case ] Looping over an enumerate
print(f'\n\t ✨ LOOPING OVER A DESCENDING RANGE:')
enumerate_range_50_60 = enumerate(list(range(50,60)))
for idx, value in enumerate_range_50_60:
  print(f'\n\t - enumerate iteration:\n\t\t index: {idx}\n\t\t value: {value} ')
  
# Practice
list_of_range_100 = enumerate(list(range(100)))
instruction = "\n\n\t 📚 PRACTICE: FROM AN ENUMERATE WITH A LIST OF 100 ITEM, GET THE INDEX OF 50"
instruction = instruction + "\n\n\t\tCreate a list from 1 to 10 and print the index of 50 is"
print( instruction )
for idx, value in list_of_range_100:
  if value == 50:
    print(f'n\t\t\tThe index of 50 is: {idx}')
