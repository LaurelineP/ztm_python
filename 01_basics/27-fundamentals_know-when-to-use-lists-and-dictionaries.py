###################  KNOW WHEN TO USE LISTS AND DICTIONARIES   ###################
# A List has order with indexes
# A Dictionary has no order and has more information accessing
# a specific key to return a certain value

dictionary_character = {
  'weapons': ['katana', 'kunai'],
  'greeting': 'Ohayo Gozaimasu',
  'is_with_magic': True,
}

print(f'\n\t---------------------KNOW WHEN TO USE LISTS AND DICTIONARIES: ---------------------')

print(f'\n\t\tOriginal variable dictionary_character: \n\t\t{dictionary_character}')

dictionary_entries =' \n\t\t- '.join(dictionary_character)
print(f'\n\t\tdictionary_character keys: \n\t\t- {dictionary_entries}')