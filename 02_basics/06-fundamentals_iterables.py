################### ITERABLES ###################

print(f'\n\t--------------------- ITERABLES: ---------------------')

# Iterables
description = f'\n\t[ List, Sets, Tuples, String, Dictionary ] are iterables'
description = f'\n\tAn object that can be accessed item by item'
print( description )

print('\n\t---------------------------------------------------')

# dictionary user 
user = {
  "name": "Lilou",
  "age": "unknown",
  "can_swim": False,
}

print(f'\n\t LOOPING ON DICTIONARIES:')

# Getting each keys of the dictionary using a for loop
print(f'\t 🔸 [ KEY ] - Would return each key/value pair\'s key\n')
for key in user:
    print(f'\t\t - returns a dictionary\'s "key": {key}')

# Getting the key/value pairs using a for loop and dictionary.keys()
print(f'\n\t  + Would return each key/value pair\'s value')
user_keys = user.keys()
for key2 in user_keys: 
  print(f'\t\t - returns the dictionary\'s "key": {key2}')

  
# Getting each values of the dictionary using a for loop and dictionary.values()
print(f'\n\t 🔸 [ VALUE ] - Would return each key/value pair\'s value')
user_values = user.values()
for value in user_values: 
  print(f'\t\t - returns the dictionary\'s "value": {value}')

# Getting the key/value pairs using a for loop and dictionary.items()
print(f'\n\t 🔸 [ KEY/VALUE ] - Would return each key/value pair\'s value')
user_items = user.items()
for tuple in user_items: 
  print(f'\t\t - returns the dictionary\'s "key/value" pair in a tuple: {tuple}')
  # unpacking which could be done within the for loop
  key, value = tuple
  print(f'\t\t - unpacking tuple to display both key: "{key}" and value: "{value}"\n')
  


  
