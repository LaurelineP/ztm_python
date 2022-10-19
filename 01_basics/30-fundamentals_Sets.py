###################  SETS   ###################
# Sets are unordered collection of unique objects - no duplicated values
# Syntax declaration: {<value>, <value>, <value>}
# Does not Supports squared brackets notation
# Supports methods: [.add(<value>)m .clear]
# Turn a list to a set and remove duplicate : set([])
# Sets methods: https://www.w3schools.com/python/python_ref_set.asp
# Sets exercise: https://repl.it/@aneagoie/sets

set1 = {1,2,3,4,5,5}
set2 = {4,5,6,7,8,9,10}

print(f'\n\t--------------------- SETS: ---------------------')
print(f'\n\tSets are unordered collection of unique objects')
print('\n\tSyntax declaration: {<value>, <value>, <value>}')
print('\n\tOriginal set1 = {1,2,3,4,5,5} returns unique set:', set1)
print('\n\tOriginal set2 = {4,5,6,7,8,9,10} returns unique set:', set2)

print('\n\t---------------------------------------------------')

print(f'\n\t- Accessing with squared brackets "list(set1)[0]" returns: {list(set1)[0]}')


# set.difference(<set>) - gets the difference between 2 sets
print(f'\n\n\t\tDIFFERENCE BETWEEN 2 SETS:') 
print(f'\t\t - set1.difference(set2) returns: {set1.difference(set2)}' )


# set.discard(<value>)
print(f'\n\n\t\tDISCARD AN EXISTING VALUE:') 
print(f'\t\t - set1.discard(5) returns: \n\t\t ---> {set1.discard(5)} \n\t\t ---> {set1}' )


# set.difference_update(...): removes all different elements of another set from this set
print(f'\n\n\t\tREMOVE ALL ELEMENT OF ANOTHER SET FROM THIS SET:') 
print(f'\t\t - set1.difference_update(set2) returns: \n\t\t ---> {set1.difference_update(set2)} \n\t\t ---> {set1} \n\t\t ---> {set2}' )


# set.intersection(<set>): gets the items in common
set1.add(4)
set1.add(5)
print(f'\n\n\t\tSAME ITEMS IN BOTH SETS - INTERSECTION:') 
print(f'\t\t - set1.intersection(set2) returns: \n\t\t ---> {set1.intersection(set2)} \n\t\t ---> {set1} \n\t\t ---> {set2}' )
print(f'\n\t\t - shorthand "set1 & set2 " returns: \n\t\t ---> {set1 & set2} ' )



# set.isdisjoint(<set>): check if nothing is in common to 2 sets
print(f'\n\n\t\tCHECK IF NOTHINS IS IN COMMON BETWEEN 2 SETS:') 
print(f'\t\t - set1.isdisjoint(set2) returns: \n\t\t ---> {set1.isdisjoint(set2)} \n\t\t ---> {set1} \n\t\t ---> {set2}' )

# set.union(<set>): concatenate 2 sets
union = set1.union(set2)
print(f'\n\n\t\tADD ANOTHER SET TO A SET:') 
print(f'\t\t - set1.union(set2) returns: \n\t\t ---> {union} \n\t\t ---> {set1} \n\t\t ---> {set2}' )
print(f'\n\t\t - shorthand "set1 | set2 " returns: \n\t\t ---> {set1|set2} ' )


# set.issubset(): is part of the bigger set
subset = set1.issubset(union)
print(f'\n\n\t\tCHECKING SET IN ANOTHER SET - ISSUBSET :') 
print(f'\t\t - set1.issubset(union) returns: \n\t\t ---> {subset} \n\t\t ---> {set1} \n\t\t ---> {union}' )



# set.issupperset(): is the bigger set and has smaller set
print(f'\n\n\t\tCHECKING A BIGGER SET HAVING A SMALLER SET :') 
print(f'\t\t - union.issuperset(set1) returns: \n\t\t ---> {union} \n\t\t ---> {set1}' )