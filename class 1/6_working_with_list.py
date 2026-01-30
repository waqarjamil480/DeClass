temp_lis = []

magicians = ['alice', 'david', 'carolina', 'alice']

magicians.count('alice')

for magician in magicians:
    print(f'Hello {magician}!')

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Avoiding Indentation Errors
# for statement in a loop. If you forget, Python will remind you:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# Making Numerical Lists
# Using the range() Function
for value in range(0,5,2):
    print(value)


# Using range() to Make a List of Numbers

numbers = list(range(1, 6))
print(numbers)


# simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)


# Working with Part of a List
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

print(players[1:])

print(players[:3])

print(players[:5])

print(players[:-1])



# Looping Through a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:") 
for player in players[:3]:
    print(player.title())


# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
print(my_foods)
temp_foods = my_foods
print(temp_foods)
temp_foods.remove('pizza')
print(temp_foods)
print(my_foods)
id(my_foods)
id(temp_foods)

my_new_list = my_foods
my_foods[0] = 'burger'
friend_foods = my_foods[:]
print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods)