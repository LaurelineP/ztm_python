###################  LISTS  ###################
# Lists are objects accissible by pointing them 
# with their index

list1 = [0, 1, 2, 3, 6]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [3, 19, 'a', True, ['one', 'two', 'three']]

# Accessing a List with their index <list>[<index>]
result_firstValueOfList1 = str(list1[0])
result_thirdValueOfList2 = str(list2[2])
result_lastValueOfList3 = str(list3[-1])

print(f'\n - Last index of list1: {result_firstValueOfList1}')
print(f'\n - Last index of list2: {result_thirdValueOfList2}')
print(f'\n - Last index of list3: {result_lastValueOfList3}')
