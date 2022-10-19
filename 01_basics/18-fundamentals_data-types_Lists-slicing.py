###################  LISTS SLICING ###################
# Lists are objects accissible by pointing them 
# with their index
#  Exercise: https://replit.com/@aneagoie/lists#main.py
print(f'\n LIST SLICING\n\t: List can use slicing like string but also List is mutable')

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes',
]
print(f'\n - Original List:" {amazon_cart}')

# Mutating an item in a list by replacing the existing one
amazon_cart[0] = 'laptop'
print(f'\n - mutating a list by pointing the index and assigning \n\ta new value "amazon_cart[0] = \"laptop\"\n\tResult:" {amazon_cart}')

# List can be sliced
sliced_amazon_cart = amazon_cart[0:3]
print(f'\n - mutating a list by pointing the index and assigning \n\ta new value "amazon_cart[0:3]\"\n\tSlice value:" {sliced_amazon_cart} \n\tList being mutated:{amazon_cart}' )

# shallow copy of a list
new_list = amazon_cart
print(f'\n - copying by assigning ( copies from object in memory ) \n\tthe List to a new variable\n\t and do another mutation will affect the original List.\n\t The Copy:" {new_list}')

new_list[0] = 'gum'
print(f'\n - The copy after mutation:{new_list}' )

# deep copy of a list 
print(f'\n - To create a real copy without afecting other object we apply a slice' )
list_copy = amazon_cart[:]
list_copy[0] = "shoes"

print(f'\n - Original cart ( not copied ):{ amazon_cart }' )
print(f'\n - Copied cart with mutation applies:{ list_copy }' )


