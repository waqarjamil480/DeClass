# Arithmetic operators (+ - * /)

a, b, c = 1, 2, 3

add = 1 + 2
print(add)

sub = 5 - 2
print(sub)

mul = 3 * 7
print(mul)

div = 10 / 5
print(div)

# Assignment operators =

box1 = 1
box2 = box1
box2 = 3
print(box1)
print(box2)

# Comparison operators (< <= == >= >)

num1 = 5
num2 = 6

print(num1 < num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 > num2)
print(not(num1 == num2))
print(num1 != num2)


# Logical operators (and or)

hasTicket = True
age = 19

canEnterInPark = hasTicket and age >= 18
print(canEnterInPark)


# Membership (in) 
customer_query = 'This product is highly recommended'
'highly recommended' in customer_query


customer_query = 'This is product is was very poor'
'highly recommended' in customer_query


# Identity (is) operators
a = [1, 2, 3]
b = a

print(a is b)        # True – both point to the same object
print(a == b)        # True – values are also equal

# Same content but different memory references
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)        # True – same content
print(a is b)    

# to check none value
x = None

if x is None:
    print("x has no value")