###################  BUILT-IN FUNCTIONS AND METHODS  ###################
# "Built-in" term in programming refers to programming
# languages providing you some tools without having to install them
# - functions are the functions being executable in standalone
# - whereas methods are the functions being executable from an object
# https://www.w3schools.com/python/python_ref_string.asp
# https://docs.python.org/3/library/functions.html
print('\nBUILT-IN: \n refers to programming languages \n providing you some tools without having to install them')
print('\nFUNCTIONS: \n are the functions being executable in standalone \n')
print('\METHODS: \n are the functions being executable from an object \n')
# Seen built-in functions
# - print()  : prints a value on the console
# - int()    : creates a number
# - str()    : creates a string
# - type()   : checks the type of a value
# - len()    : get the length of a value

# Seen methods
# - format

quote = 'To be or not to be...'
print(f'\n0. "quote" original value: {quote}' )

print(f'\n1. "quote" original value of `quote.upper()\n returns quote with all letters in uppercase`: {quote.upper()}' )

print(f'\n2. "quote" original value of `quote.capitalize()`\n returns quote with the first letter in uppercase: {quote.capitalize()}' )

print(f'\n3. "quote" original value of `quote.lower()\n returns quote with all letters in lowercase`: {quote.lower()}' )

print(f'\n3. "quote" original value of `quote.find("be")`\n returning index of the starting point of the word`: {quote.find("be")}' )

print(f'\n4. "quote" original value of `quote.replace("be", "ME")`\n returning all words matching "be" to be replaced by "ME"`: {quote.replace("be", "ME")}' )

print(f'\nIMMUTABILITY --> applyind those string modification would not persist\n as strings are immutable')
print(f'- `quote`: {quote}')

quote2 = quote.replace("be", "ME")
print(f'- `quote2 with the mutated string stored within`: {quote2}')