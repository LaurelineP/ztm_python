# REPLIT
Replit is an interface running a rep with basics environment needs.
This meeans this has the back environment of programming languages to  
kick start some course straight away.  
( includes interpreters, compiler, the language itself )
However this is not the same as running in into one's own environment  
as we do not have access that freely to the terminal  

Ex: command to run a file
`python <path-file>.py`
The environment mainly runs main.py  no other paths unless we provide config.
```sh
run="python 01_basics/01-fundamentals_discovering-python.py"
run="python 01_basics/02-fundamentals_data-types-number.py"
run="python 01_basics/03-fundamentals_math-functions.py"
run="python 01_basics/04-fundamentals_operator-precedence.py"
```



## Configure Replit
### Enabling Replit to run a specific page
- .replit file: either you replace run command opening by default a path  
  resource: https://replit.com/talk/ask/How-to-run-another-python-file-not-the-mainpy/29188
  WARNING: the .replit file approach does not last between session which mean each time you have to instruct replit to run the updated command
- either you import your code to run with main ( mentioned in above URL )


# DEVELOPER FUNDAMENTALS
Don't read the dictionary: Do not read and learn everything about a  
programming languages: know only what exists in order to get back to it  
instead of memorizing it


# INDENTATION IN PYTHON
Identation and spaces are important with Python turning it mandatory
whereas in other languages it is not and is mainly relate to enhance
code readability
The Python interpretor considers spaces ( space or tab ) with meanings
to interprete the code

https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# OOP
Object Oriented Programming is a 
Every thing is an objects - Object have methods and attributes on their own
We can create our own types

OOP is a paradigm to structure the code in order to    
ease to maintainability.
Breaking up the code in smaller pieces (*in objects*) in order to have those objects enable to be worked on separately

https://en.wikipedia.org/wiki/History_of_programming_languages

## VOCABULARY WITH CLASS
- instanciate: fact to associate a class to a variable

## CUSTOM OBJECT / TYPE
Can create our own type using `class` keyword (Advanced/OOP)['./03_advanced-python_OOP/01_OOP.py']
### Under __init__
Lines with self => will associate dynamic attributes

### METHODS
All functions defined within and starting with `def`
are methods that will be available for all instance

### DECORATORS
#### @classmethod 


#### @static methods



## FUNDAMENTAL
Always test your assumptions: test what your learning


## 4 PILLARS OF OOP
### ENCAPSULATION
4 OOP pillars
- encapsulation: 
It's a binding of data in functions that manipulates that data.
We encapsulate in one big object
Those data within and functions are what is called attributes and methods
Represents the ability en encapsulating the functionality of a class X ( object ) by having its own properties and functionalities
Those functions are able to access the data within this very same object ( self )

#### Why wanting to encapsulate data ( attributes and function ) to an object ?
In order to rely on the existing data and being able to reuse them any time needed
A class without any functions ( just the attributes ) is useless as it only serve to store the data like a dictionary would
would.
The **only difference** with a dictionary it is how the dev accesses it 
```py
class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Bracket notation accessing attribute "name" 's value
player_class = Player('Majo', 1000 )
print(player_class['name'])

# Dot notation accessing key "name" 's value
player_dict = { "name": "Majo", "age": 1000 }
print(player_dict.name)
```

### ABSTRACTION
Principle of hiding the full implementation of an object or function, for instance, in order to being able to use the provided attributes or methods ( from a class ) without caring how it is implemented.
In Python there are no reserved keyword for privacy concept however there is a nomenclature.
This nomenclature is to have _ ( an underscore ) before the variable or function or attributes ...

### INHERITANCE
Principle to inherit attributes and methods from another object and being able to exploit them within the defined object calling a class for instance.

A class can also inherit from another class which 
will provide the base definition with which one can
compose from with new ones ( attributes and/or methods )

### POLYMORPHISM
The ability to redefine an attributes or methods 
from the inherited object.
- User class as a base class can have a method attack
- A deviant class such as a specific kind of User like a character Wizard (class) can inherit from User but can also defined, in its encapsulation,
it's own attack method --> this would override the User attack method 


# FP
Functional programming
- History of Functional Programming: https://en.wikipedia.org/wiki/History_of_programming_languages