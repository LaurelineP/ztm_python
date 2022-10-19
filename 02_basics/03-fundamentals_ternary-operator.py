###################  TERNARY OPERATOR  ###################
# ( Aka Condition expression )
# Shorthand to small logic flow 


print(f'\n\t--------------------- TERNARY OPERATOR: ---------------------')
conditional_keywords_str = " \n\t\t---> ".join(['if', 'elif', 'else'])
print(f'\n\tTernary ( or Condition expression ) are shorthands to if...elif...else flow')
print(f'\n\tTernary is available to Python since 2.4' )
print(f'\n\t - Syntaxt: \n\t\t---> "<condition_if_true> if <condition> else <condition_if_else>"')

print('\n\t---------------------------------------------------')


# Add conditional logic with a boolean to control 
# the flow of your code
age_input = input('\t\tWhat is your age ? ')
has_license_input = input('\t\tDo you have a driver license ? ')

is_old_enough = int(age_input) > 18
is_licensed = has_license_input == 'yes' or  has_license_input == 'Yes'

# Can you drive?
# ----------------------------------------------
# result = ''
# if is_old_enough and is_licensed:
#    result = '🚙 You can already drive !'
# elif is_old_enough:
#   result = '📚 You can learn to drive'
# else:
#  result = '✋ Nope, not yet'
# ----------------------------------------------

result = '🚙 You can already drive !' if is_old_enough and is_licensed else '✋ Nope, not yet'

print(f'\n\t- Opinion about driving ---> {result}')