# A Simple Dictionary

var_dict = dict()
var_dict = {}
print(var_dict)
print(type(var_dict))

person = {
    "name": "mike",
    "age": 28, 
    "subjects": ['Maths', 'Physics']
}

print(person.get('height'))

person['subjects'][1]

products = [
    {
        'product_name': 'airpods',
        'product_desc': 'Active Noise Cancellation'
    },
    {
        'product_name': 'smart watch',
        'product_desc': 'Active Noise Cancellation'
    },
    {
        'product_name': 'headphones',
        'product_desc': 'Active Noise Cancellation'
    }
]

for product in products:
    product_key, product_value = product.items()


print(person['subjects'][1])

# example of a unstructured data as list of dict
dic = [
    {"name":"mike","age":28},
    {"name":"asdfsa","age":28},
    {"name":"adsfa","age":28},
    {"name":"werer","age":28},
]

var_dict = {
    "name": "mike",
    "class": "CDE",
    "course": "python",
    "num": 10,
    "bool": True,
    "list_data": ['one', 2, 3],
    "dict": { 'key' : 'value' }
}

print(var_dict)

print(var_dict['name'])
var_dict['name1']
var_dict.get('name1', 'this is default value')

var_dict['list_data']

var_dict.get('id', "no data returned")
var_dict['id']

var_dict.keys()
var_dict.values()
var_dict.items()

# [
#     ('name', 'mike'), 
#     ('class', 'CDE'), 
#     ('course', 'python'), 
#     ('num', 10), 
#     ('bool', True), ('list_data', ['one', 2, 3])]

for obj in var_dict:
    print(obj)
    
for obj in var_dict.keys():
    print(obj)

for obj in var_dict.values():
    print(obj)

for key, value in var_dict.items():
    print(f"key is: {key} and values is: {value}")


for x, y, z in [(1,2,3), (4,5,6), (7,8,9)]:
    print(x, y, z)

for k in var_dict.keys():
    print(k, var_dict[k])
    
for v in var_dict.values():
    print(v)

for key, value in var_dict.items():
    print(f"for key: {key} we have value: {value}")


alien_0 = {
    'color': ['green','blue'],
    'points': 5
}

print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

print(alien_0.get('colors'))
# alien_0['color_1']
# alien_0.get('color_1')


student = {
    'name': 'Mike',
    'marks': [70, 80, 90, 10],
    'age': 25
}

sum_of_marks = sum(student['marks'])
count_of_subjects = len(student['marks'])


print(f'Student Name is {student["name"]} and age is {student["age"]} and his average is = {sum_of_marks/count_of_subjects}')

# Working with Dictionaries

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
new_dict_to_add = {'key1':'value1', 'key2':'value2'}
alien_0.update(new_dict_to_add)
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = dict()
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed. 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    # This must be a fast alien.
    x_increment = 3
print(x_increment)
# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0)
print(alien_0['points'])
del alien_0['points']
print(alien_0)


# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python'
}
for obj in favorite_languages:
    print(obj)

for key in favorite_languages.keys():
    print(key)

for value in favorite_languages.values():
    print(value)

for key, value in favorite_languages.items():
    print(key, value)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for key, value in favorite_languages.items():
    print(key, value)


# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'not found ') 
print(point_value)

# # # Looping Through a Dictionary

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi',
}

user_0.keys()

user_0.values()
user_0.items()

for key in user_0.keys():
    print(key)

for value in user_0.values():
    print(value)

user_0.items()

for key, value in user_0.items():
    # print(key_value)
    print(f"\nKey: {key}") 
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
}

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

# Looping Through a Dictionary’s Keys in a Particular Order
favorite_languages = { 
    'jen': 'python','sarah': 'c', 'edward': 'ruby', 'phil': 'python', 
    }
for name in sorted(favorite_languages.keys()): 
    print(f"{name.title()}, thank you for taking the poll.")


favorite_languages = {
    'jen': ['python','c','c#'],
    'sarah': ['c','Java'], 
    'edward': 'ruby', 
    'phil': ['python', 'js']
}

for name, lang in favorite_languages.items():
    print(f"{name} fav lang is:")
    if isinstance(lang, str):
        print(f'- {lang}')
    else:
        for lan in lang:
            print(lan)

# jen fav lang is:
#  - python
#  - c
#  - c#

# Looping Through All Values in a Dictionary
favorite_languages = { 
    'jen': 'python',
    'sarah': 'c', 'edward': 'ruby', 'phil': 'python', 
    }
print("The following languages have been mentioned:") 
for language in favorite_languages.values():
    print(language.title())

# sets

languages = {'python', 'ruby', 'python', 'c'} 
languages

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
       print(alien)


# A List in a Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'], 
}

users = {
    'name': 'mike',
    'address': 'KAI'
}


for key,value in pizza.items():
    if key == 'crust':
        print(f"Pizza crust: {pizza['crust']}")
    if key == 'toppings':
        for toping in value:
            print(f"Pizza toping: {toping}")
    if key == 'user':
        print(f"User Name: {value['name']}")
    

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# jen fav languages are:
#     python
#     ruby
# sarah fav language is:
#     C#
# ....
# ....


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c#',
    'mike': 'c',
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'], 
}

for name, languages in favorite_languages.items():
    if isinstance(languages, str):
        print(f"{name} fav language is:")
        print("1.", languages)
    else:
        print(f"{name} fav languages are:")
        for i, lang in enumerate(languages):
            print(f"\t {i+1}. {lang}")

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is:")
    if isinstance(languages, list):
        print('\n'.join(languages))
    else:
        print(languages)
    print()

    
    
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is:")
    if isinstance(languages, list):    
        for language in languages:
            print(language)
    else:
        print(languages)
        
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is:")
    if isinstance(languages, list):    
        print(languages[1])
    else:
        print(languages)




for name, languages in favorite_languages.items(): 
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

for name, languages in favorite_languages.items(): 
    print(f"\n{name.title()}'s favorite languages are:")
    print(' & '.join(languages))



# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein', 
        'location': 'princeton', 
    },
    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # print(user_info)
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}") 
    print(f"\tLocation: {location.title()}")

# User Input and While loop

name  = 'mike'
last_name = name 
last_name = 'tyson'


names = ['mike ', 'usama']
copy_names = names.copy()

del copy_names[0]


# unpacking a dictionary
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

person = {'name': 'Alice', 'age': 25}

greet(**person)  # Unpacks: greet(name='Alice', age=25)
