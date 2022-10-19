# A variable
# 🔸 ( JS eq.: var myVar = ... )
myVar = 'Lowla\'s'

# Logs the chain of caracters
# 🔸 ( JS eq.: console.log(...) )
print('1 - ' + myVar + 'print')

# Prompt a interactive message and catches the value
# 🔸 ( JS eq.: confirm(...) )
# - step 1: discovering how it behave
input('2 - Behavior test - What is your name? ')

# - step 2: input use case:
#           holding the returned value received from the input
#           then, logging the returned value
inputValue = input(
  '3 - Use case: catching & storing value - What is your name? ')

print('4 - Input\'s value printed: ' + inputValue)
