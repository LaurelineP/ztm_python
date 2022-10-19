###################  DATA TYPES LIST UNPACKING   ###################
# Dictionaries are object to other programming language
# An unorder list of key/value pair
#   - key must be non-mutable data-types
#   - value could be anything

dictionary = {
  'a': 1,
  'b': 2,
  'c': '3',
  1: 'one',
}
print(f'\n\t--------------------- DICTIONARIES: ---------------------')
print(f'\n\n\t\tUnnorder list of key/value pair where\n\t\t key must be a string or a number and value \n\t\tcan be anything')
print(f'\n\t\tOriginal:{dictionary}')
print('\n--------------------------------------------------------------')

print(f'\n\n\t\tACCESSING ITEM:')
print(f'\t\t- We access elements within using square \n\t\tbrackets notations with the exact key value \n\t\t( a UNIQUE non-mutable data-types /  a not UNIQUE would reassign the prior one whith the last assignation )')
accessing_str = "dictionary[1]"
accessing_str_KO = "dictionary['1']"
result_accessing_str = dictionary[1]
print(f'\t\t- Accessing {accessing_str} returns: {result_accessing_str}')
print(f'\t\t- Accessing {accessing_str_KO} returns an error: "KeyError: \'1\'"')