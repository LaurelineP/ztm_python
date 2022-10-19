###################  LIST METHODS   ###################
#  List methods: https://www.w3schools.com/python/python_ref_list.asp

print(f'\n\tLIST METHODS:\n\t\t List built-in methods')

list_methods = ['append', 'extend', 'insert', 'pop', 'remove', 'clear']

# original List
basket = [1,2,3,4,5]
print(f'\n\tOriginal List: {basket}')

print('\n--------------------------------------------------------------')

# append: adds an item to the end of the list ( not returning the object modified )
# --> .append(<item>)
returned_append = basket.append(6)
print(f'\n\t - .append(<item>): Adds item at the end of the List\n\t"basket.append(6)" \n\t\t- modification result: {basket}\n\t\t- returns: {returned_append}')

# insert: adds an item anywhere within the list ( not returning the object modified )
# --> .insert(<index>, <item>)
returned_insert = basket.insert(0, 0)
print(f'\n\n\t - .insert(<index>, <item>): Adds item anywhere within the List\n\t"basket.insert(0, 0)",  \n\t\t- modification result: {basket}\n\t\t- returns: {returned_insert}')

# extend: adds multiple items in the list
# --> .extend([<item>,<item>, ...]) ( not returning the object modified )
returned_extend = basket.extend(['...', 10, 11])
print(f'\n\n\t - .extend([<item>, <item>]): Adds items at the end of the List\n\t"basket.extend(["...", 10, 11])"\n\t\t- modification result {basket}\n\t\t- returns: {returned_extend}')

# pop: removes the last or indexed item of the list
# --> .pop([<index>]) ( returns a the popped value )
returned_pop = basket.pop()
print(f'\n\n\t - basket.pop(): Removes the item at a specific index of the List\n\t"basket.pop()"\n\t\t- modification result {basket},\n\t\t- returns: {returned_pop}')

returned_pop_index = basket.pop(-3)
print(f'\n\n\t - basket.pop(<index>): Removes the item at a specific index of the List\n\t"basket.pop(-3)"\n\t\t- modification result {basket},\n\t\t- returns: {returned_pop_index}')

# remove: removes the indexed item of the list
# --> .remove(<value>) ( returns a the removed value )
returned_remove_value = basket.remove('...')
print(f'\n\n\t - remove.remove(<value>): Removes the VALUE at a specific index of the List\n\t"basket.remove("...")"\n\t\t- modification result {basket},\n\t\t- returns: {returned_remove_value}')

# clear: removes everything in the list
# --> .clear() ( returns a the removed value )
returned_remove_value = basket.clear()
print(f'\n\n\t - remove.clear(): Removes everything in the List\n\t"basket.clear()"\n\t\t- modification result {basket},\n\t\t- returns: {returned_remove_value}')

print('\n\n--------------------------------------------------------------')
print(f'\n\t\t\t\t\t METHODS COVERED HERE\n\t {list_methods}')
