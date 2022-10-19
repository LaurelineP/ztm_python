###################  STRING INDEXES  ###################
# https://repl.it/@aneagoie/string-indexes
# Knowing that a string is an order chain of caracters
# Underneath the hood: strings are stored in the computer memory 
# analysing each caracters and their positions
print('\nSTRING INDEXES: \n Each caracters within a string is stored in the computer memory \n to restitute each letter position in order to allow accessing them')


sentence = 'me me me'
print(f'\n1. "sentence": {sentence}' )
# would attributes index for each caracters
# INDEX | CORRESPONDING LETTER
# 0     | m
# 1     | e
# 2     | space
# 3     | m
# 4     | e
# 5     | space
# 6     | m
# 7     | e

# Accessing one letter with "[index]"
print(f'"sentence" first letter accessed by "sentence[0]":', sentence[0]) # m


# Accessing a range of letters [index-start: index-stop-excluded]
print(f'"sentence" ( string slicing ) range of 2 letters accessed by "sentence[0:2]":', sentence[0:2]) # me 


# Accessing a range of letters with "a step over" [index-start: index-stop-excluded: stepover]
# stepover being the number of caracter to jum to
string_of_digits='0123456789'
string_range='0123456789'[0:5]
print(f'"string_of_digits" first letter accessed with "string_of_digits[0:4:1]": "' + string_of_digits[0:5:2] +'"') # 0 2 4

print('\nThis is like saying between 012345, gets 0 then the second number from 0 \n and so on as long as it is within the range \n ( getting 2 to 2 letters )')

print(f'"string_of_digits" range of first caracter to the end with "string_of_digits[0:]":', string_of_digits[0:]) # 0123456789 

print(f'"string_of_digits" range of all caracter before index 5 included with "string_of_digits[:5]":', string_of_digits[:5]) # 01234

print(f'"string_of_digits" range of first caracter to the end with "string_of_digits[5:]":', string_of_digits[5:]) # 56789 

print(f'"string_of_digits" range of first caracter to the end taking every 2 caracters with "string_of_digits[0::2]":', string_of_digits[0::2]) # 02468

print(f'"string_of_digits" last caracter with "string_of_digits[-1]":', string_of_digits[-1]) # 56789 

print(f'"string_of_digits" revert string\'s letters with "string_of_digits[-1]":', string_of_digits[::-1]) # 9876543210 