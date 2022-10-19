###################  LIST METHODS   ###################
# Exercise: https://repl.it/@aneagoie/lists-
# Python keywords: https://www.w3schools.com/python/python_ref_keywords.asp


print(f'\n\tLIST METHODS 2:\n\t\t List built-in methods')

list_methods = ['index', '<value> in <list>', 'count']

# original List
basket = ['a','b','c','d','e']
print(f'\n\tOriginal List: {basket}')

print('\n--------------------------------------------------------------')

# index: gets the index of the known value in the list ( returning the index of the occurrence - or an error if not found )
# --> .index(<value>)
returned_value = basket.index('d')
print(f'\n\t - .index(<value>): Gets the item index within a List\n\t"basket.index("d")" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_value}')

# --> .index(<value>, [<start-index>,[<end-index>]])
returned_value_fromIndex = basket.index('d',0)
print(f'\n\t - .index(<value> [<start-index>,[<end-index>]]):\n\t Gets the item index within a range in a List\n\t"basket.index("d", 0)" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_value_fromIndex}')


#  <value> in <list>: adds an item to the end of the list or string ( not returning the index of the occurrence - or an error if not found )
# --> .index(<value>, <start-index>,<end-index>)
returned_value_in_list = 'c' in basket
print(f'\n\t - <value> in <list>: Checks if a value is within a List \n\t""c" in basket" \n\t\t- returns: {returned_value_in_list}')


# .count(<value>): counts the occurence of a value in the list or string ( not returning the index of the occurrence - or an error if not found )
# --> .count(<value>)
returned_count = basket.count('e')
print(f'\n\t - .count(<value>): Counts the occurence of a value in the list or string\n\t"basket.count("e")" \n\t\t- returns: {returned_count}')

print('\n\n--------------------------------------------------------------')
print(f'\n\t\t\t\t\t METHODS COVERED HERE\n\t\t  {list_methods}')
