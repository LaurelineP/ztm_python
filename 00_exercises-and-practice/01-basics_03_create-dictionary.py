#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 

user1 = {
  "age": 100,
  "username": "Mako",
  "weapons": ['kunai', 'katana' ],
  "is_active": True,
  "clan": 'AI'
}

print(f'\n\t- All keys: {user1.keys()}')


user1.update({ 'weapons': user1['weapons'] + ['magic roll']})
user1.update({ 'is_banned': False })
user1.update({ 'is_banned': True })

user2 = user1.copy()
user2.update({'age': 0, 'username': 'Neo'})

print(f'\n\t- user1: {user1}' )
print(f'\n\t- user2: {user2}' )

































#Solutions:
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
# user = {
#     'age': 22,
#     'username': 'Shogun',
#     'weapons': ['katana', 'shuriken'],
#     'is_active': True,
#     'clan': 'Japan'
# }

#2 iterate and print all the keys in the above user.
# print(user.keys())

#3 Add a new weapon to your user
# user['weapons'].append('shield')
# print(user)

#4 Add a new key to include 'is_banned'. Set it to false
# user.update({'is_banned': False}) 
# print(user)

#5 Ban the user by setting the previous key to True
# user['is_banned'] = True
# print(user)

#6 create a new user2 my copying the previous user and update the age value and username value. 
# user2 = user.copy()
# user2.update({'age': 100, 'username': 'Timbo'})
# print(user2)