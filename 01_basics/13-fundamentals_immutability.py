###################  IMMUTABILITY  ###################
# Immutability is the idea of a changeable value for a variable
# - String in python are immutable once it is created ( not changeable )
print('\nSTRING INDEXES: \n Immutability is the idea of a non changeable value for a string')


sentence = 'Aloha'
print(f'\n0. "sentence" original value: {sentence}' )
# sentence[0] = 'R' #TypeError: 'str' object does not support item assignment
sentence = 'Hello'
print(f'\n1. "sentence" after reassigning part of the value: #TypeError: \n \'str\' object does not support item assignment' )

print(f'\n2. "sentence" after reassigning the entire value: {sentence}' )