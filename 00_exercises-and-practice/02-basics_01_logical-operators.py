###################  EXERCISE LOGICAL OPERATORS   ###################
print(f'\n\t--------------------- EXERCISE LOGICAL OPERATORS: ---------------------')

print('\n\t--------------------------------------------------------------')
is_magician = True
is_expert = False

# string to output 
magician_expert_sentence = '✨🧙‍♂️You are a master magician.'
magician_sentence = '✨🪄 At least you are getting there!'
no_powers_sentence = '🤷‍♀️ You need magic powers!'

# values
values =  f'\n\n\t Values:'
values =  values + f'\n\t\t - `is_magician`value: {is_magician}'
values =  values + f'\n\t\t - `is_expert` value: {is_expert}'
print( values )

# instructions
instruction = f'\n\n\t Check if:'
instruction = instruction + f'\n\t 1 - is a magician and an expert then print: "{magician_expert_sentence}"'
instruction = instruction + f'\n\t 2 - is a magician and not an expert then print: "{magician_sentence}"'
instruction = instruction + f'\n\t 3 - is not a magician then print: "{no_powers_sentence}"'

print( instruction )
print('\n\t--------------------------------------------------------------')


# exercise application
# ternary implementation - not the best approach due to readability
result_ternary = magician_expert_sentence if is_magician and is_expert else magician_sentence if is_magician and not is_expert else no_powers_sentence
print(f'\n\t\t - [ ternary ] Result: {result_ternary}')

# if else if else flow
result_regular = f'\n\t\t - [ if, elif, else ] Result: '
if is_magician and is_expert:
  result_regular = result_regular + magician_expert_sentence
elif is_magician and not is_expert:
  result_regular = result_regular + magician_sentence
else: result_regular = result_regular + no_powers_sentence
print( result_regular )