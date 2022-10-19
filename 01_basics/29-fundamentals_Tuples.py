###################  TRICKY COUNTER  ###################
# Tuples are like immutable list 
# --> syntax using parentheses insteadof squared bracket
# As this is an immutable value it could be used as: a dictionary key
# Each items are indexed hence it supports:
# - the squared bracket accessing, 
# - the <value> in <list>
# - the unpackaging process
# - getting the length
# - 2 similar methods [ count(<value>), index(<value>) ]
# https://www.w3schools.com/python/python_ref_tuple.asp


tuple = (1,2,3,4,5)

print(f'\n\t--------------------- TUPLES: ---------------------')
print(f'\n\tOriginal "tuple = (1,2,3,4,5)": {tuple}')

print('\n--------------------------------------------------------------')

print(f'\n\t- Accessing with squared brackets "tuple[0]" returns: {tuple[0]}')


print( tuple.index(3) )