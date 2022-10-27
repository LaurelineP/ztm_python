#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Nova', 6)
cat2 = Cat('Sylva', 1)
cat3 = Cat('Garfield', 40)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*cats):
	for cat in cats:
		print( sorted(cats, reverse = True))


get_oldest_cat(cat1, cat2, cat3)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2