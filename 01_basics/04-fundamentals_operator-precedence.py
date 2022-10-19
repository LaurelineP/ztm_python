###################   OPERATOR PRECEDENCE   ###################
 # In a calculation, we may need to use parentheses in order to  
# not mix the operations otherwise it gets calculated on  
# certains priorities
# this is the operator precedences ( like in math )
# ------------------- MATH FUNCTIONS ---------------------- #
print('\n[ OPERATOR PRECEDENCE ]')


# Without parentheses
#  - multiplication and division primes over addition and substraction
print('- multiplication and division are \nprioritised over an addition / or substraction for 20 - 3 * 4:', 20 - 3 * 4) # 8

# Here it is how it is computed and how devs should write it
print('- how it is red: 20 - (3 * 4)', 20 - (3 * 4)) # 8

# Operand order priority
# ()
# **
# * and /
# + and -

# Exercise: https://replit.com/@aneagoie/Operator-Precedence

print((5 + 4) * 10 / 2) # 45.-

print(((5 + 4) * 10) / 2) # 45.0

print((5 + 4) * (10 / 2)) # 45.0

print(5 + (4 * 10) / 2) # 25.0

print(5 + 4 * 10 // 2) # 25.0