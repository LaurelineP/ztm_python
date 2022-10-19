###################  TYPE CONVERSIONS  ###################
# 

## Program Guessing Age
# From a given year, guess the age

question_year = 'What is the year of your birth? '
birth_year = input(question_year)

result = 2022 - int(birth_year)

print(f'\nQuuestion `input(question_year)`: {question_year}\n  Response from input: {birth_year}\n Result:{result}')

print(f'\n Tricks here: input\s value is returning strings and we cannot substract integer with string \n - this is a type conversion that occurs' )
