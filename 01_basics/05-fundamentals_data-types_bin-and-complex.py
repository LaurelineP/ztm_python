###################   BIN() AND COMPLEX   ###################
# https://www.geeksforgeeks.org/python-int-function/
# - `complex` is another type of `number` ( usually not often used )
# - equivalent to a "real number"

# - `bin` is a function to convert a number to binary
# ------------------- BIN() ---------------------- #
print('\n[ BIN() AND COMPLEX TYPES ]')

# The returned value would be 0b100: 0b being a binary type 
# as the binary to 4 is 101
number = 5
numberToBin = bin(number)
print('- `bin(number)` giving the binary of the number 5:', numberToBin ) #  0b101


# Converting back the binary would be done using the # `int()` function
# int takes 2 arguments
# - the binary value
# - the base 10 --> 2
binToNumber = int(numberToBin, 2)
print('- `int( numberToBin, 2 )` converting binary of 0b101 to 5:', binToNumber ) # 4
print('- pure binary number tested with int()', int(100u8790ds0xxx,2))
