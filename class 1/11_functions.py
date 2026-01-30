# Defining a Function

def function_name():
    print('this is my function')
    
function_name()

def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 5)

def add(num1, num2):
    print(num1 + num2)

add(5, 10)

def div(num1, num2):
    '''
        This function is used to divide num1 with num2
    '''
    pass

div()

def greet_user():
    """Display a simple greeting.
    did not require any params
    """
    print("Hello!")

greet_user()

# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting with username.
    params: 
        username(string): a username to be printed
    """
    return username.title() 

new_title =  greet_user('mike tyson')

# greet_user(username='mike')


# Arguments and Parameters

# The variable username in the definition of greet_user() is an example of a parameter, 
# a piece of information the function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument
# is a piece of information that’s passed froa function call to a function.

# note People sometimes speak of arguments and parameters interchangeably. 
# Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.

# Passing Arguments

# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='dog')
describe_pet(pet_name="harry", animal_type="cat")
# describe_pet("harry","cat")

describe_pet(pet_name="harry", animal_type="cat")
describe_pet("harry", "cat")

describe_pet(pet_name='harry', animal_type='hamster')


# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')


# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type='hamster', age = 10):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    print(f"his age is: {age}")

describe_pet('cat')

def print_pizza_order(flavour, size=12):
    print(f"pizza order: {flavour} with size: {size}")
    
print_pizza_order('tikka', 6)

describe_pet('tom')

describe_pet(pet_name='tom', age=20, animal_type='cat')

def print_full_name(first, last, middle=''):
    # print(f"{first} {middle} {last}".title())
    if middle:
        print(f"{first} {middle} {last}".title())
    else:
        print(f"{first} {last}".title())


print_full_name('mike','','tyson')
print_full_name('mike','tyson')


def get_full_name(first, last, middle=''):
    return f"{first} {middle} {last}".title()

full_name = get_full_name('mike','tyson')
print(full_name)

describe_pet('tom', animal_type='cat', age=3)
# describe_pet('tom', animal_type='cat',  age=5)

describe_pet(pet_name='willie', animal_type='dog')

# # Return Values

# Returning a Simple Value

def get_formatted_name(first_name, last_name, age=10):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title(), age, []

# get_formatted_name('mike', 'tyson')

musician, age, emp_list = get_formatted_name('jimi', 'hendrix')
obj = get_formatted_name('jimi', 'hendrix')

print(emp_list)
print(musician)
print(age)


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print(age)


# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name): 
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}" 
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker') 
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    # if middle_name:
    full_name = f"{first_name} {middle_name} {last_name}"
    # # else:
    #     full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name(first_name='jimi', last_name='hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} 
    return person

musician = build_person('jimi', 'hendrix')
musician = build_person(first_name='jimi', last_name='hendrix')
print(musician)

# # Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list.""" 
    for name in names:
        msg = f"Hello, {name.title()}!" 
        print(msg)

usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)

def make_pizza(*toppings):
    print(toppings)

make_pizza('topping1', 'topping2')

def make_pizza(*toppings):
    print('User order a Pizza with:')
    for top in toppings:
        print(top)

make_pizza('topping1','topping2','topping3')
def make_pizza(pizza_name, *toppings):
    print(f'User order a Pizza: {pizza_name} with:')
    for top in toppings:
        print(top)

make_pizza('tikka')
make_pizza('tikka','topping1','topping2')

def make_name(*name):
    n = ''
    for i in name:
        n+=' '+i
    print(n)

make_name('m','mike','tyson', 'asfdasdf')

make_pizza('ing1', 'ing2','ing3')

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested.""" 
    print(toppings)
    print(type(toppings))
    for topping in toppings:
        print(topping)

make_pizza('top1', 'top2')

make_pizza('pepperoni',[1,2,3],('a','b','c'))
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested.""" 
    print(f"size of pizza is: {size}")
    # print(toppings)
    # print(type(toppings))
    for topping in toppings:
        print(topping)

make_pizza(10)
make_pizza(10, 'top1', 'top2')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make.""" 
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings:
        print(f"- {topping}")

make_pizza()
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: 
        print(f"- {topping}")

make_pizza(16)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    print('first', first)
    print('last', last)
    for info, value in user_info.items():
        if info == 'phone':
            if not isinstance(value, int):
                print('wrong phone type')
        print(info, value)

build_profile(first='mike', last='tyson', age=10, phone=12345)

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # print(user_info)
    # print(type(user_info))
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(build_profile('albert', 'einstein', dept="physics", age="40"))

build_profile(
    'albert', 'einstein', 
    location='princeton',field='physics'
)

def arb_params(**kwargs):
    if kwargs.get('username'):
        print("this is my username: ", kwargs['username'])
    """Build a dictionary containing everything we know about a user."""
    print(kwargs)

arb_params(one = '1', two=2 , username='mike')

# print(user_profile)



def build_profile(**user_info):
    """Build a dictionary containing everything we know about a user."""
    # user_info['first_name'] = first
    # user_info['last_name'] = last
    return user_info

build_profile(location = 'paris', field = 'physics')
build_profile()



# lambda functions
power = lambda x: x ** 2
power(4)

# lambda function with map
numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(power, numbers))
print(squared)   # Output: [1, 4, 9, 16]


# lambda function with filter
numbers = [1, 2, 3, 4, 5, 6]
remainder = lambda x: x % 2 == 0
even = list(filter(remainder, numbers))
print(even)  # Output: [2, 4, 6]


# lambda function with sorted
words = ["banana", "apple", "cherry", "date"]

sorted_words = sorted(words, key=lambda word: len(word), reverse=True)
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']