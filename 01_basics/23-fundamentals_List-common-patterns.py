###################  LIST COMMON PATTERNS   ###################
#  Exercise: https://repl.it/@aneagoie/lists-3
#  
print(f'\n\tLIST COMMON PATTERNS:\n\t\t List built-in methods')
original_list = [ 'n', 'e', 'd', 'x', 'r']
print(f'\n\t\tOriginal list: {original_list}')
print('\n--------------------------------------------------------------')


# len() : Figuring out the length of the List
print(f'\n\n\tLEN: Get the length of a list: \n\t - Length is: {len(original_list)}')

print(f'\n\n\n\tREVERSING A LIST:')

result_reversed = original_list.reverse()
print(f'\t - Reversing with `reverse` affecting the List itself:\n\t {original_list}')

result_slicing = original_list[::-1]
print(f'\t - Reversing by "slicing" returning a NEW list:\n\t {result_slicing}')


print(f'\n\tSORT A LIST:')
print(f'\t- Sort using Sort:{original_list.sort()}')



my_range = range(1,10)
list_from_range = list(my_range)

print(f'\n\tRANGE :')
print(my_range)
print(f'\t- range(...) built-in function :\n\t `range(1,10)` return { my_range }')
print(list_from_range)
print(f'\t- range built-in function :\n\t `list(range(1,10))` return { list_from_range }')

print(f'\n\JOIN :')
sentence = ' '.join(["hi", "my", "name", "is", "Lowla"])
print(f'\t- <string>.join(<list>) will take every item \n\t\t to concatenate to the string - each iteration will \n\t\t append the referenced <string> :\n\t `" ".join(["hi", "my", "name", "is", "Lowla"])` return {sentence}')
