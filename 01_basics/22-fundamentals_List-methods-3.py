###################  LIST METHODS 3   ###################
# Exercise: https://repl.it/@aneagoie/lists-
# Python keywords: https://www.w3schools.com/python/python_ref_keywords.asp


print(f'\n\tLIST METHODS 3:\n\t\t List built-in methods')

list_methods = ['sort', 'reverse', 'copy']

# original List
basket = ['7','w','0','r','g']
print(f'\n\tOriginal List: {basket}')

print('\n--------------------------------------------------------------')

# sort: sorts the order of the list [ number string first then letters or numbers] ( not returning anything - or an error if not found )
# --> .sort()
returned_sort = basket.sort()
print(f'\n\t - .sort(): Sorts the order of the list [ number strings first, then letters or numbers ]\n\t"basket.sort()" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_sort}')


# sorted built-in function: sorts the order of the list [ number string first then letters or numbers] and returns a new array
# --> sorted(<list>)
returned_sorted = sorted(basket)
print(f'\n\t - sorted(basket): Sorts the order of the list [ number strings first, then letters or numbers ] and returns a NEW list \n\t"basket.sort()" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_sorted}  \n\t\t- is a different list - "basket.sort() == basket.sort()": {basket.sort() == basket.sort()}')



# reverse: reverses the order of the list [ number string first then letters or numbers] ( not returning anything - or an error if not found )
# --> .sort()
returned_reverse = basket.reverse()
print(f'\n\t - .reverse(): Reverse the order of the list \n\t[ letters first, then  number strings or numbers ]\n\t"basket.reverse()" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_reverse}')


# copy: copies a list and returns a NEW LIST
returned_copy = basket.copy()
print(f'\n\t - .copy(): copies a list\n\t"basket.reverse()" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_copy}\n\t\t - is a different list: { basket == basket.copy()}')

print('\n\n--------------------------------------------------------------')
print(f'\n\t\t\t\t\t METHODS COVERED HERE\n\t\t  {list_methods}')
