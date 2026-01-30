A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)               # {1, 2, 3, 4, 5, 6}
print(A.union(B))          # Same result

# Intersection
print(A & B)               # {3, 4}
print(A.intersection(B))   # Same result

# Difference
print(A - B)               # {1, 2}
print(B - A)               # {5, 6}

# Symmetric Difference
print(A ^ B)               # {1, 2, 5, 6}


# subset and superset
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True


# Removes duplicates
user_input = input("Enter numbers separated by space: ")
numbers = set(user_input.split())

print("Unique numbers:", numbers)
