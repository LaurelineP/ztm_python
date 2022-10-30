###################  DICTIONARY METHODS   ###################
# Exercise Repl: https://repl.it/@aneagoie/dictionary

dictionary_character = {
  'weapons': ['katana', 'kunai'],
  'greeting': 'Ohayo Gozaimasu',
  'is_with_magic': True,
}

print(f'\n\t--------------------- DICTIONARY METHODS: ---------------------')
print(f'\n\t\tOriginal variable dictionary_character: \n\t\t{dictionary_character}')
print(f'\n\t\tDictionary methods link:\n\thttps://www.w3schools.com/python/python_ref_dictionary.asp')

print('\n--------------------------------------------------------------')



# - "<list>.get(<string>)": accessed the dictionary and returns a the value and 
# prevent from computing any error if the key is not there by returning "None" instead
character_get_age = dictionary_character.get('age')
character_age_str_KO = "\"dictionary_character['age']\" returns an error"
character_get_age_str = f"\"dictionary_character.get('age')\" returns: \n\t\t\t ---> {character_get_age} "

# dictionary[<key>] and dictionary.get(<key>)
print(f'\n\n\t\tACCESSING A DICTIONARY WITH SQUARED BRACKET AND WITH GET METHOD:') 
print(f'\t\t - {character_age_str_KO}')
print(f'\t\t - {character_get_age_str}')

# <key> in <object>
print(f'\n\n\t\tCHECKING EXISTANCE OF A KEY IN DICTIONARY:')
is_key_in_dictionary = 'age' in dictionary_character
is_key_in_dictionary_str = f"\"'age\' in dictionary'\" returns: \n\t\t\t ---> {is_key_in_dictionary}"
print(f'\n\t\t - {is_key_in_dictionary_str}')

# list of keys: dictionary.keys() ( getting all dictionary keys )
list_of_key = dictionary_character.keys()
list_of_key_str = f'"dictionary_character.keys()" returns:\n\t\t\t ---> {list_of_key}'
print(f'\n\t\t - {list_of_key_str}')


# list of values: dictionary.values() ( getting all dictionary values of each key )
list_of_values = dictionary_character.values()
list_of_values_str = f'"dictionary_character.values()" \n\t\t\treturns (to use with <value> in <dictionary>): \n\t\t\t ---> {list_of_values}'
print(f'\n\t\t - {list_of_values_str}')


# list of items: dictionary.items() ( getting an entire key/value pair)
list_of_items = dictionary_character.items()
list_of_items_str = f'"dictionary_character.items()" returns:\n\t\t\t ---> {list_of_items}'
print(f'\n\t\t - {list_of_items_str}')


# copying all list: dictionary.copy()
character_copy = dictionary_character.copy()
character_copy_str = f'"dictionary_character.copy()" returns:\n\t\t\t ---> {character_copy} \n\t\t\t ---> is equal to the original: {character_copy == dictionary_character}'
print(f'\n\t\t - {character_copy_str}')

# clearing all dictionary: dictionary.clear()
character_copy_clear = character_copy.clear()
character_copy_clear_str = f'"character_copy.clear()" returns:\n\t\t\t ---> {character_copy_clear}\n\t\t\t ---> original: {dictionary_character}\n\t\t\t ---> copy: {character_copy}'
print(f'\n\t\t - {character_copy_clear_str}')

# removes a key/value pair by a key in dictionary: dictionary.pop(<key>)
dictionary_character_pop = dictionary_character.pop('is_with_magic')
dictionary_character_pop_str = f'"dictionary_character.pop(\'is_with_magic\')" returns:\n\t\t\t ---> popped value returned: {dictionary_character_pop}\n\t\t\t ---> original: {dictionary_character}'
print(f'\n\t\t - {dictionary_character_pop_str}')

# removes last ( since python 3.7 - before it was randomly ) key/value pair by a key in dictionary: dictionary.popitem()
dictionary_character_popItem = dictionary_character.popitem()
dictionary_character_popItem_str = f'"dictionary_character.popitem()" returns:\n\t\t\t ---> last ( since python 3.7/ before it was randomly ) \n\t\t\t\t popped value returned: {dictionary_character_popItem}\n\t\t\t ---> original: {dictionary_character}'
print(f'\n\t\t - {dictionary_character_popItem_str}')

# update a key/value pair in dictionary: <dictionary>.update({'<key>': <new-value>})
dictionary_character_update = dictionary_character.update({'roar': 'rrr'})
dictionary_character_update__str = "dictionary_character.update({roar': 'rrr'})"
dictionary_character_update_str = f"{dictionary_character_update__str} returns:\n\t\t\t ---> updated value returned: {dictionary_character_update}\n\t\t\t ---> original: {dictionary_character}"
print(f'\n\t\t - {dictionary_character_update_str}')

dictionary_character_update2 = dictionary_character.update({'roar': 'grrr'})
dictionary_character_update2__str = "dictionary_character.update({'roar': 'grrr'})"
print(f'\t\t\t ---> updating "roar" again: {dictionary_character}')

