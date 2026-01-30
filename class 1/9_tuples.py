# unpacking tuples
person = ("Alice", 25, "Designer")

name, age, profession = person

print(name)       # Alice
print(age)        # 25
print(profession) # Designer

# unpacking with variable length
numbers = (1, 2, 3, 4, 5)

a, b, *c = numbers

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
