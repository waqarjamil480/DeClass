game_lives = 10

# while loop example
while game_lives > 0:
    print(game_lives)
    game_lives -= 1

names = ['Alice', 'Joe', 'Peter']

# for each loop
for name in names:
    print(name)

for index, name in enumerate(names):
    print(f'{index} - {name}')

# for with range
for i in range(len(names)):
    print(names[i])


# for with range
for i in range(1, len(names)):
    print(names[i])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
# for with range and stepping value
for i in range(2, len(nums), 2):
    print(f'Skipped {nums[i]}')

# break
for i in range(0, len(nums)):
    if i == 4:
        break
    print(i)

# continue
for i in range(0, len(nums)):
    if i == 4:
        continue
    print(i)

# pass
for i in range(0, len(nums)):
    if i == 4:
        pass
    print(i)

# for with dictionary
dic = {
    'name': 'Mike Tyson',
    'age': 25
}

for k, v in dic.items():
    print(f'{k} = {v}')


for k in dic.keys():
    print(f'{k}')

for v in dic.values():
    print(f'{v}')