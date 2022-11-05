# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Nova', 6)
cat2 = Cat('Sylva', 1)
cat3 = Cat('Garfield', 40)
cat4 = Cat('Romuald', 13)


# 2 Create a function that finds the oldest cat
def get_oldest__advanced(*cats):
    """
    Using max built-in function and lambda (not seen yet)
    - `max` with a second argument key with a lambda
    """
    cat_max_age = max(cats, key=lambda cat: cat.age)
    return cat_max_age


def get_oldest__basic(*cats):
    """
    Using max built-in function and regular loops
    - `max` regular
    """
    age_list = []
    for cat in list(cats):
        age_list.append(cat.age)
    max_age = max(age_list)
    age_index = age_list.index(max_age)
    return cats[age_index]


older_cat__advanced = get_oldest__advanced(cat1, cat2, cat3, cat4)
older_cat__basic = get_oldest__basic(cat1, cat2, cat3, cat4)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {older_cat__basic.name} is {older_cat__basic.age} years old.')
