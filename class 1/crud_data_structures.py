# LIST CRUD OPERATIONS

# CREATE
my_list = [10, 20, 30]
print("Created List:", my_list)

# READ
print("Read second item:", my_list[1])  # 20

# UPDATE
my_list[1] = 25
print("Updated second item:", my_list)

# DELETE
del my_list[0]
print("Deleted first item:", my_list)


# TUPLE CRUD OPERATIONS

# CREATE
my_tuple = (10, 20, 30)
print("Created Tuple:", my_tuple)

# READ
print("Read first item:", my_tuple[0])

# UPDATE - ❌ Not allowed (Immutable)
# my_tuple[1] = 40  → This will raise TypeError

# DELETE - ❌ Not allowed (Immutable)
# del my_tuple[0]  → This will raise TypeError

# You can "update" a tuple by converting it to a list
temp = list(my_tuple)
temp[1] = 99
my_tuple = tuple(temp)
print("Updated Tuple (via conversion):", my_tuple)



# SET CRUD OPERATIONS

# CREATE
my_set = {1, 2, 3}
print("Created Set:", my_set)

# READ (Loop or Membership Test)
print("Is 2 in set?", 2 in my_set)

# UPDATE
my_set.add(4)
print("Added 4:", my_set)

my_set.update([5, 6])
print("Updated with multiple values:", my_set)

# DELETE
my_set.remove(1)  # Raises error if not found
print("Removed 1:", my_set)

my_set.discard(99)  # No error if not found
print("Tried discarding 99 (safe):", my_set)

my_set.clear()
print("Cleared Set:", my_set)



# DICTIONARY CRUD OPERATIONS

# CREATE
my_dict = {'name': 'Alice', 'age': 25}
print("Created Dict:", my_dict)

# READ
print("Read 'name':", my_dict['name'])

# UPDATE
my_dict['age'] = 26
print("Updated 'age':", my_dict)

my_dict['city'] = 'Karachi'
print("Added 'city':", my_dict)

# DELETE
del my_dict['name']
print("Deleted 'name':", my_dict)


removed = my_dict.pop('city')
print("Popped 'city':", removed)
print("Final Dict:", my_dict)
