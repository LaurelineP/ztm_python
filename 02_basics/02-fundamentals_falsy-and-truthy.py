###################  TRUTHY AND FALSY  ###################
# Underlying process of python is to evaluate values
# - to be kind of true
# - to be kind of false



print(f'\n\t--------------------- TRUTHY AND FALSY: ---------------------')

stackoverflow_link = "https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false"

print(f'\n\t - Stackoverflow question about Falsy and Truthy: \n\t\t---> {stackoverflow_link}')


print('\n--------------------------------------------------------------')
print(f'\n\tOriginal variables:')
my_string = "This is a string"
my_empty_string = ""

my_string_str='my_string = "This is a string"'
my_empty_string_str='my_empty_string = ""'

print(f'\n\t - `my_string`: {my_string_str}')
print(f'\n\t - `my_empty_string`: {my_empty_string_str}')


print('\n--------------------------------------------------------------')

print(f'\n\t - `my_string` would be considered as truthy - `bool(my_string): `', {bool(my_string)})
print(f'\n\t - `my_empty_string` would be considered as falsy - `bool(my_empty_string): `', {bool(my_empty_string)})
