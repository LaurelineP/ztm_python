################### WALRUS OPERATORS  ###################
print(f'\n\t-------------------  WALRUS OPERATORS -------------------')
NEW_LINE = '\n\t'

# Description
description = f"{ NEW_LINE } Walrus operators are recent python features"
description += f"{ NEW_LINE } These are used within expression to momentarily store a value reused in the code"
description += f"{ NEW_LINE } Course's link: https://repl.it/@aneagoie/walrus#main.py"
print( description )

print('\n\t------------------------------------------------')

def use_walrus_operator():
  collection = [0, 1, 2, 3]

  if( (n:= len( collection)) > 2):
    print(f'{ NEW_LINE }If length > 2: Collection has len {n} and its bigger than 2')
    while (length:= len(collection )) > 2:
      collection = collection[:-1]
      print(f'{ NEW_LINE } - Collection sliced by one', collection)
    else:
      print(f'{ NEW_LINE }Reduced array to 2? Job done! 🙌')
    


use_walrus_operator()
