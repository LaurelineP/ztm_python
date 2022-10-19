###################  TRCIKY COUNTER   ###################
print(f'\n\t---------------- EXERCISE TRICKY COUNTER: ----------------')
instruction = '\n\t\t'
instruction = instruction + "Build a counter that sum each number in a list using a for loop"
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_str = "\n\t\t - numbers = [1,2,3,4,5,6,7,8,9,10]"
print( instruction + numbers_str )

print('\n\t --------------------------------------------------------')

sum = 0
for number in numbers:
  sum += number

print(f'\n\t Sum result: {sum}')