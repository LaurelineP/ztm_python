###################   Numbers with "int" and "float"   ###################

# ------------------- INTEGER OPERATIONS ---------------------- #
# 01 - Integer Numbers: whole numbers without decimal
print('[ EXPLORING INTEGER AND CALCULATIONS ]')
print(' - Sums (2 + 5):', 2 + 5) # 7
print(' - Substracts (2 - 5):', 2 - 5) # -3
print(' - Multiplies (2 * 5):', 2 * 5) # 10
print(' - Divides (2 / 5):' , 2 / 5) # 0.4
print(' - Powers (2 ** 5):' , 2 ** 5) # 25

# Double divides rounds down to the result of a regular division
print(' - Double divides rouding down to integer 0 with (2 // 5):' , 2 // 5) # 0
print(' - Double divides rouding down to integer 1 with (5 // 5):' , 5 // 5) # 1

# Modulos - calculating the remainder of a division (% operator)) returning integer
print(' - Modulo of (2 % 5):' , 2 % 2) # 0





# ------------------- TYPES OF NUMBERS: INT AND FLOAT ---------------------- #
# Testing the type of a value ( type() )
print('\n[ TESTING TYPES OF NUMBERS ] - int and float')
print(' - Tests type of (2 + 5)', type(2 + 5)) # <class 'int'>
print(' - Tests type of (2 - 5)', type(2 - 5)) # <class 'int'>
print(' - Tests type of (2 * 5)', type(2 * 5)) # <class 'int'>
print(' - Tests type of (2 / 5)', type(2 / 5)) # <class 'float'> ( because has a decimal )

# Divide by 0: returns an error: "ZeroDivisionError: division by zero" and kills the server
# print(' - Tests type of (2 / 0)', type(2 / 0))
