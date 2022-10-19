###################   VARIABLES   ###################
# variable are elements to which we assign values
# in order to store the value and reuse it later



# ---------------- CONVENTIONS ------------------
# 🐍 snake_case: in variable you cannot uses spaces 
# to express multiple words: this is where you
# would use snake_case with an underscore in between

#  snake case variable
print('\n\n\n1 - SNAKE_CASE:\n  In programmation and variables\n  there are no use of the space character,\n this is where the "_" ( underscore ) is used')
my_snake_case_variable = "I am a snaked cased variable value"
print('  - "my_snake_case_variable" variable:', my_snake_case_variable)



# 🏁 Start your variable using lowercase or _undescore
# There are other conventions that we can see in programming ( variable starting with uppercase or full word in uppercases )
 # 0 - let's say it is a number who never changes
NUMBER = 5

# 1 - based on that number never changing I know I will use it
my_number=NUMBER # 

# 2 - Here I would like to use it within a bigger 
# implementation but telling other devs not to
# communicate it outside of that bigger implementation
_my_private_number=my_number
print('\n\n\n2 - HOW TO START THE VARIABLE:\n  with lowercase or uppercase / without underscore \n  or with underscore gives another meaning \n  to how a dev reads the code')
print( '\n  - a variable that should not be modified; \n  to be aknowlegde while coding for a related\n  feature using "NUMBER":', NUMBER )
print( '\n  - a custom variable I use but has meaning just for\n  me ( not mandatory for others to aknowlegde\n  for a new other feature ) - "my_number":' , my_number )
print( '\n  - a variable that should not be modified - NUMBER:' , NUMBER )

# 🔡 ̲🔢 Letters, underscore, and number can be used for
# defining the name of a variable

number = 0
number0 = number
my_number0 = number
print('  ( all result are the same; \n  here it shows how we could name a variable \n  with the authorised and recommended caracters')
print('  - "number":', number)
print('  - "number0":', number0)
print('  - "my_number0":', my_number0)

print('\n\n\n3 - HOW TO START WRITTING THE VARIABLE NAME:\n  with lowercase or uppercase / without underscore \n  or with underscore gives another meaning \n  to how a dev reads the code')



# 🔡🔠 case sensitive: the fact that when 
# defining a variable it is important 
# to pay attention to letters being 
# uppercase or lowercase
my_name = 'lowla lowercased'
my_Name = 'LOWLA uppercased'
print('\n\n\n4 - CASE SENSITIVE:\n  printing the same reading words with a different case use')
print('  - prining "my_name":', my_name )
print('  - prining "my_Name":', my_Name )



# 🔃 do not override the keywords
# Like mentions, the programming language has 
# its own nomenclatures, following those would
# help avoiding breaking the the program as some
# keyword a specially dedicated to Python itself

# print( True = "true") # returns "cannot assign to True" and break the program
print( '\n\n\n5 - DO NOT OVERRIDE RESERVED KEYWORDS\n  Reserved keywords are words already used \n  within the Python itself, trying overriding \n  them would break your code ')
print( '-  print( True = "true"): returns "cannot assign to True" \n  and breaks the program')