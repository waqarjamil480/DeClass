import math

print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.1415926535...
print(math.factorial(5)) # 120

import random

print(random.randint(1, 10))       # Random integer between 1 and 10
print(random.choice(['a', 'b']))   # Randomly pick one item
print(random.shuffle([1, 2, 3, 4])) # Shuffle list in place

import pandas

import datetime

now = datetime.datetime.now()
print("Current time:", now)

birthday = datetime.datetime(1999, 10, 12)
age = now - birthday
print("Age in days:", age.days / 365)