# -------------------- LIST CONVERSIONS --------------------

# List to Dictionary (from list of tuples)
pairs = [('a', 1), ('b', 2)]
print("List to Dict:", dict(pairs))  # [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}

# List to Dictionary (from two separate lists)
keys = ['name', 'age']
values = ['Alice', 30]
print("List to Dict (zip):", dict(zip(keys, values)))  # ['name', 'age'] + ['Alice', 30] → {'name': 'Alice', 'age': 30}

# List to Dictionary (using index as key)
fruits = ['apple', 'banana']
print("List to Dict (index):", {i: fruit for i, fruit in enumerate(fruits)})

# List to Tuple
my_list = [1, 2, 3]
print("List to Tuple:", tuple(my_list))  # [1, 2, 3] → (1, 2, 3)

# List to Set
my_list = [1, 2, 2, 3]
print("List to Set:", set(my_list))  # [1, 2, 2, 3] → {1, 2, 3}

# -------------------- TUPLE CONVERSIONS --------------------

# Tuple to List
my_tuple = (10, 20, 30)
print("Tuple to List:", list(my_tuple))  # (10, 20, 30) → [10, 20, 30]

# Tuple to Set
my_tuple = (1, 2, 2, 3)
print("Tuple to Set:", set(my_tuple))  # (1, 2, 2, 3) → {1, 2, 3}

# Tuple to Dictionary (tuple of tuples)
pair_tuple = (('a', 100), ('b', 200))
print("Tuple to Dict:", dict(pair_tuple))  # (('a', 100), ('b', 200)) → {'a': 100, 'b': 200}

# -------------------- SET CONVERSIONS --------------------

# Set to List
my_set = {4, 5, 6}
print("Set to List:", list(my_set))  # {4, 5, 6} → [4, 5, 6] (unordered)

# Set to Tuple
print("Set to Tuple:", tuple(my_set))  # {4, 5, 6} → (4, 5, 6)

# -------------------- DICTIONARY CONVERSIONS --------------------

# Dict to List of Keys
my_dict = {'x': 9, 'y': 8}
print("Dict to List (keys):", list(my_dict.keys()))  # → ['x', 'y']

# Dict to List of Values
print("Dict to List (values):", list(my_dict.values()))  # → [9, 8]

# Dict to List of Tuples
print("Dict to List (items):", list(my_dict.items()))  # → [('x', 9), ('y', 8)]

# Dict to Tuple of Tuples
print("Dict to Tuple (items):", tuple(my_dict.items()))  # → (('x', 9), ('y', 8))

# Dict to Set of Keys
print("Dict to Set (keys):", set(my_dict))  # → {'x', 'y'}

# Dict to Set of Tuples (items)
print("Dict to Set (items):", set(my_dict.items()))  # → {('x', 9), ('y', 8)}

# -------------------- COMBINED EDGE CASES --------------------

# Set of Tuples to Dictionary
tuple_set = {('id', 1), ('age', 20)}
print("Set to Dict (tuples):", dict(tuple_set))  # → {'id': 1, 'age': 20}

# Tuple of Lists to List of Tuples
tuple_of_lists = ([1, 2], [3, 4])
print("Tuple of Lists to Tuple of Tuples:", tuple(tuple(i) for i in tuple_of_lists))

# List of Sets to List of Lists
list_of_sets = [{1, 2}, {3, 4}]
print("List of Sets to List of Lists:", [list(s) for s in list_of_sets])
