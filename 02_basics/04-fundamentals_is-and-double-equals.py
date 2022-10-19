###################  IS AND DOUBLE EQUALITY ###################

print(f'\n\t--------------------- IS AND DOUBLE EQUALITY: ---------------------')
conditional_keywords_str = " \n\t\t---> ".join(['if', 'elif', 'else'])
print(f'\n\tTernary ( or Condition expression ) are shorthands to if...elif...else flow')
print(f'\n\tTernary is available to Python since 2.4' )
print(f'\n\t - Syntax: \n\t\t---> "<condition_if_true> if <condition> else <condition_if_else>"')

print('\n\t---------------------------------------------------')


# checking double equality
print(f'\n\n\tChecking double equality:')
print( f'\t - "True == 1":\t {True == 1 }') # True
print( f"\t - \"'' == 1\": \t {'' == 1}")   # False
print( f'\t - "[] == 1": \t {[] == 1}')   # False
print( "\t - \"10 == 10.0\"\t", 10 == 10.0 )# True
print( "\t - [] == []\t\t", [] == [] )  # True

# checking is equality
print(f'\n\n\tChecking is equality:')
print( f'\t - "True is 1":\t {True is 1 }') # False
print( f"\t - \"''is 1\": \t {'' is 1}")   # False
print( f'\t - "[] is 1": \t {[] is 1}')   # False
print( "\t - \"10 is 10.0\"\t", 10 is 10.0 )# False
print( "\t - [] is []\t\t", [] is [] )  # False