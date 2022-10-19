###################  CONDITIONAL LOGIC   ###################
# Conditional logic combines condition keywords and boolean value
# Careful about indentation
# - if
# - elif
# - else
# will process the first condition met then stop


print(f'\n\t--------------------- CONDITIONAL LOGIC: ---------------------')
conditional_keywords_str = " \n\t\t---> ".join(['if', 'elif', 'else'])
print(f'\n\tConditional keywords combined to boolean creates conditional logics evaluations')
print(f'\n\t - Conditional keywords: \n\t\t---> {conditional_keywords_str}')

print('\n\t---------------------------------------------------')


# Add conditional logic with a boolean to control 
# the flow of your code
age_input = input('\t\tWhat is your age ? ')
has_license_input = input('\t\tDo you have a driver license ? ')

is_old_enough = int(age_input) > 18
is_licensed = has_license_input == 'yes' or  has_license_input == 'Yes'

result = ''
# Can you drive?
if is_old_enough and is_licensed:
   result = '🚙 You can already drive !'
elif is_old_enough:
  result = '📚 You can learn to drive'
else:
 result = '✋ Nope, not yet'



print(f'\n\t- Opinion about driving ---> {result}')