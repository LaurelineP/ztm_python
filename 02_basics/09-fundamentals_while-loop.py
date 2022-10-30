################### WHILE LOOP (1) )###################
print(f'\n\t--------------------- WHILE LOOP (1): ---------------------')
NEW_LINE = '\n\t'

# Description
description = NEW_LINE + 'A while loop is a loop evaluating a truthy condition'
description = description + NEW_LINE + 'and stop only when the condition is not met anymore'
description = description + '\n' + NEW_LINE + '⚠️  Have to be careful to ensure while looping the initial'
description = description + NEW_LINE + 'condition mets a falsy evaluation to exit that loop'
description = description + NEW_LINE + 'otherwise this enter into an infinite loop'

description = description + f'\n\n\t 🔸 Syntax: `while(<truthy-condition>):`'
description = description + f'\n\n\t 🔸 `break` keyword: exits the loop or potential infinite loop ✨'

description = description + f'\n\n\t 🔸 `else` keyword: can be used in order to output something'
description = description + f'\n\t\t after a while loop exit with a falsy condition met ✨'

print( description )

print('\n\t--------------------------------------------------------')


# While loop in practice  [ Use case ] Looping over an enumerate
print(f'\n\t ✨ WHILE LOOP IN PRACTICE:')
i = 0 
while( i < 10 ):
 # increment over the loop will at somepoint met the condition 
 # 10 < 10 outputing false and will exit the loop
  sentence_iteration = f'\t\t - current value: {i} / incrementing `i` by one before next iteration: { i + 1 }'
  sentence_last_iteration = f'{ sentence_iteration }\n\n\t\t\t ---> LAST iteration exiting the condition because'
  sentence_last_iteration = sentence_last_iteration + NEW_LINE + f'\t\t`i` being 10: this is not inferior to 10: {i + 1 < 10}'
  i += 1 
  print( sentence_last_iteration if (not i < 10)  else sentence_iteration )
else: print(f'{NEW_LINE} \t Else statetement occuring when the initial condition is not met: \n\t\t✨Loop is done!')

  
################### WHILE LOOP (2) )###################
print(f'\n\n\n\t--------------------- WHILE LOOP (2): ---------------------')


description = f'{ NEW_LINE } 🔸 When to use while loop or for loops?'
description = f'{ description }{ NEW_LINE }\t - if you need a mere loop go for a for loop'
description = f'{ description }{ NEW_LINE }\t - if you don\'t know how many time you want to loop,{NEW_LINE}\t\tgo for a while loop to combine either with {NEW_LINE}\t   `break` or `else` keywords'
print( description )