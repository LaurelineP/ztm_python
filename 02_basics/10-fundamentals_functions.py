################### FUNCTIONS ###################
NEW_LINE = '\n\t'

# function definition and execution
def explain_function():
  print('\n\t---------------------------------------------------')
  print(f'\t--------------------- FUNCTIONS: ------------------')
    # function definition for say_hello
  def say_hello():
    return(f'👋 Hello')
  # Function
  definition = f'{NEW_LINE}A function allows to have a stored process in one{NEW_LINE}object to exectute any times we want{NEW_LINE}Relates to DRY principle'
  definition += f'{NEW_LINE}\n\t 🔸 A function needs to be defined with `def` keyword{NEW_LINE}\tbefore being able to be called '
  definition += f'{NEW_LINE}\n\t 🔸 A function needs to be executed to compute the code{NEW_LINE}\twithin its defintion: by calling the function{NEW_LINE}\t --> with the parentheses followed by ":"'
  definition += f'{NEW_LINE}\n\t 🔸 Syntax for function definition: `def <function-name>([ parameters ]):`'
  definition += f'{NEW_LINE}\n\t 🔸 Printing the function would give the object in memory:{NEW_LINE}\t\t{say_hello}'
  definition += f'{NEW_LINE}\n\t 🔸 To return a value use `return` keyword { NEW_LINE } Note: any code below this return would not be executed'
  
  print( definition )
  
  print('\n\t---------------------------------------------------')
  
  
  # Executing the function
  result = say_hello()
  
  function_def_str = "\"def say_hello(): print('👋 Hello')\""
  function_exec_str = "say_hello()"

  # Example
  description = f'{ NEW_LINE } Example:'
  description += f'{ NEW_LINE }\t - Function definition: {function_def_str}'
  description += f'{ NEW_LINE }\t - Function execution: {function_exec_str}'
  description += f'{ NEW_LINE }\t - RESULT: {result}'
  
  print( description )



# function parameters and arguments
def explain_function_parameters_and_arguments():
  print('\n\n\n\t---------------------------------------------------')
  print(f'\t------------ PARAMETERS AND ARGUMENTS: ------------')
  definition = f'{ NEW_LINE }As suggested in the function syntax, it is possible'
  definition += f'{ NEW_LINE }to render the function more dynamic.'
  definition += f'{ NEW_LINE }This is done by:'
  definition += f'{ NEW_LINE }\t 🔸 defining,in the function definition context'
  definition += f'{ NEW_LINE }\t\t what is called "parameters";'
  definition += f'{ NEW_LINE }\t 🔸 while executing the function, the value(s)'
  definition += f'{ NEW_LINE }\t\twe provide (for the definition parameter(s)'
  definition += f'{ NEW_LINE }\t\tare called "argument(s)"'
  print( definition )
    
  print('\n\t---------------------------------------------------')

  def say_hello_to(name): return(f'👋 Hello, {name}!')

  function_defintion_with_parameters_str = '"def say_hello_to(name): return(f"👋 Hello, {name}!)"'
  function_execution_with_arguments_str = "\"say_hello_to('Smith')\""

  # Example
  print(f'{ NEW_LINE }Example:')
  print(f'\t\t - "parameter" (name) in function definition: {NEW_LINE}\t\t --> {function_defintion_with_parameters_str}')
  print(f'\n\t\t - "argument" ("Smith") in function execution: {NEW_LINE}\t\t --> {function_execution_with_arguments_str}')

  result = say_hello_to('Smith')
  print(f'\n\t\t - RESULT: {result}')
# function definition and execution syntax


def explain_default_parameters_and_keywords():
  print('\n\n\n\t---------------------------------------------------')
  print(f'\t---------- DEFAULT PARAMETERS AND KEYWORDS --------')
  definition = f'{ NEW_LINE }So far we\'ve been using "positional parameters and arguments"'
  definition += f'{ NEW_LINE }( because the variable in the definition are reached thanks'
  definition += f'{ NEW_LINE }to the argument order between parentheres )'

  definition += f'\n{ NEW_LINE }🔸 Another way to provide those would be with the "keyword arguments"'
  definition += f'{ NEW_LINE }by defining the expected name variable equal to a value'

  definition += f'\n{ NEW_LINE }🔸 Default arguments: are fallbacks parameter in the { NEW_LINE }function definition that would applie if no arguments were provided"'
  definition += f'{ NEW_LINE }by defining the expected name variable equal to a value'
  print( definition )
    
  print('\n\t---------------------------------------------------')
  
  # Example
  # function definition ( positional parameter )
  def say_hello_with_a_smiley_to(name="Goat", emoji="🐐"):
    return f'👋 Hello {name} {emoji}!'

  # function execution ( keyword arguments )
  result_with_arguments = say_hello_with_a_smiley_to(emoji='😛', name="Smith")
  result_without_arguments = say_hello_with_a_smiley_to()

  function_definition_str = "\"def say_hello_with_a_smiley_to(name=\"Goat\", emoji=\"🐐\"):\n\t\t\t\t\treturn f'👋 Hello {name} {emoji}!'\""
  functin_execution_str = "say_hello_with_a_smiley_to(emoji = '😛', name = \"Smith\")"

    
  print(f'{ NEW_LINE }Example:')
  print(f'\t\t - function definition: { NEW_LINE }\t\t --> {function_definition_str}')
  print(f'\n\t\t - keyword arguments given unordered" ("Smith") in function execution: { NEW_LINE }\t\t --> { functin_execution_str }')
  print(f'{ NEW_LINE }\t - RESULT with arguments: { result_with_arguments }')
  print(f'\t\t\t (Bad practice to purposely not follow the definition order)')
  print(f'{ NEW_LINE }\t - RESULT without arguments: { result_without_arguments }')
  





# def explain_function_return_keyword():
  



explain_function()
explain_function_parameters_and_arguments()
explain_default_parameters_and_keywords()