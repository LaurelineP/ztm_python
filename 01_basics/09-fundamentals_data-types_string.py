###################  ESCAPE SEQUENCES  ###################


print('\n1. DATA TYPE STRING - PAIR OF QUOTES:\n Strings can be initiated with both\n a pair of single or double quotes wrapping the chain of caracter ')

# Pair of Single quotes
my_string_singleQuote = 'Hello World created as follow: \'...\''
print('\n - "my_string_singleQuote" value:\n  ', my_string_singleQuote) # 'Hello World from my_string_singleQuote'

# Pair of Double quotes
my_string_doubleQuotes = "Hello World created as follow: \"...\""
print('\n - "my_string_doubleQuotes" value:\n  ', my_string_doubleQuotes) # Hello World from my_string_doubleQuote




print('\n\n\n2. DATA TYPE STRING - BUILT IN FUNCTION STR:\n Strings can be initiated with  a built in function `str` \n accepting, as parameter, other data-types to transforms \n them as strings')

# Built-in function `str()`
my_str_100 = str(100)

# Ensuring `my_str_100` is string typed
my_str_type = type( my_str_100 )
print('\n - `my_str_100` value:', my_str_100, '\n   being a string of type: ', my_str_type)




print('\n\n\n3. DATA TYPE STRING - PAIR OF TRIPPLE SINGLE QUOTES:\n Strings can be initiated using the following for multiline\n long strings: \'\'\'\n   This is an example of string 1\n   This is an example of string 2\n  \'\'\'')
my_long_string = '''MMM
   O _
   ---
'''
print('\n - "my_long_string" value":\n  ', my_long_string) # Hello World from my_string_doubleQuote



print('\n4. DATA TYPE STRING - CONCATENATION:\n An existing variable with a string can use the "plus" \n operator to add another bit of string to it')
my_initial_string = "Hello"
my_second_string = 'Lowla'
my_concatenation= my_initial_string + ', ' + my_second_string
print('\n - "my_concatenation" value concatenating\n  `my_initial_string` + ", "+`my_concatenation` value:\n  ', my_concatenation) # Hello World from my_string_doubleQuote
