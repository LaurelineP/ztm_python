###################  LIST UNPACKING   ###################
# Unpacking is the way to assignate multiple 
# values to dedicated variable - 
#  ( similar to the result of JS destructuring )
#  
collection = [1, 2, 3, 4, 5, 6, 7]
print(f'\n\n\t\tOriginal:{collection}')

a, b, c, *others, d = collection
print(f'\t Unpacking: is the way to assignate multiple values to dedicated variables \n\t Each values are assigned thanks to their index according to the number of variable')
print(f'\t Syntax: <variable>,<variable> = [<value>, <value>]')
print(f'\t Syntax: The in-between unspecified value should be a variable prepended by *: ')
print(f'\t Example: "a, b, c, *others, d = collection": ')

print(f'\t - a: {a}')
print(f'\t - b: {b}')
print(f'\t - c: {c}')
print(f'\t - others: {others}')
print(f'\t - d: {d}')