###################  PASSWORD CHECKER  ###################
# 

## Program Password Checker
# - Get the username
# - Get the password
# - Get the password 
# - Turn all password characters with a * caracter
# - Print the final result with:
#   - each password caracters transformed with *
#   - the length of the password *
# - EXTRA Check if the length is at least 8 caracters


inputUsername = 'Pick a username: '
inputPassword = 'Pick a password: '

usernameValue = input( f'\n{inputUsername}' )
passwordValue = input( inputPassword )

passwordLength = len(passwordValue)
passwordValueMultiplied = '*' * passwordLength

has8Caracters = len(passwordValue) >= 8

print(f'\n\nResult Pasword check checking username, password length and hidden password:\n\n - username value: {usernameValue} \n - password length: {passwordLength} \n - password hidden: { passwordValueMultiplied }\n - password has sufficient number of caracters: { has8Caracters }')
