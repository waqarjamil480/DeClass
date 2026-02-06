# value= int(input("Enter a number to find if it is available in list or not: "))
# list = [1,2,3,4,5,6,7,8,9,10]
# len(list)
# x=0 
# while x <len(list):
# 	print(f"value in list:{list[x]} index:{x} in list")
# 	if (list[x] == value):
# 		print(f"User Value:{value}, finded on:{x}. in list")
    
# 	x +=1

# table_number = int(input("Enter Number of Table you want to show"))
# print(f"Table of:{table_number} is required")
# count = 1
# while count <= 10:
# 	print(f"{table_number} X {count} = {count*table_number}")
# 	count +=1


# table_number = int(input("Enter Number of Table you want to show:"))
# till_number = int(input("enter number till when you want to show table:"))
# print(f"Table of:{table_number} is required")
# count = 1
# while count <= till_number:
# 	print(f"{table_number} X {count} = {count*table_number}")
# 	count +=1


# print all elements in a list using loop 
# list = [1, 2, 5, 10, 45, 24, 3, 1, 33]
# count = 0
# while count< len(list):
# 	print(f"Index:{count} value:{list[count]}")
# 	count +=1


# counter= 1
# while counter <=100:
# 	print(counter)
# 	if(counter == 10):
# 		break
# 	counter +=1



# list= [10, 13, 14, 15, 16, 7, 18, 19, 25]
# x = 7
# counter = 0
# while counter < len(list):
# 	if(list[counter] == x):
# 		print(f"value:{x} found on: {counter} position of list")
# 		break
# 	else:
# 		print("finding...")
# 	counter +=1 


# counter = 0
# while counter<= 10:
# 	if(counter == 3):
# 		counter +=1
# 		continue
# 	print(counter)
# 	counter += 1


# while True:
#     choice = input("Type Y to print the line again (any other key to stop): ")

#     if choice.upper() == 'Y':
#         print("This line is printed again!")
#     else:
#         print("Program stopped.")
#         break

# list= [10, 13, 14, 15, 16, 7, 18, 19, 25]
# for i in list:
#     if i == 15:
#         print("found 15")
#         break
#     print(i)
# else:
#     print("end")

# for i in range(5):
# 	print(i)


# dollar=int(input("Enter Amount in US Dollar : "))
# def usd(a):
#     s=int(280)
#     d=a*s
#     print (f"{a} USD CONVERT IN PKR IS {d}")

# usd(dollar)



# num = int(input("Enter a number : "))

# def check(num):
#     if(num%2==1):
#         print(f"{num} is ODD")
#     else:
#         print(f"{num} is Even")
#     return

# check(num)





# n = int(input("Enter Number : "))
# def waqar(n):
#     if(n==0):
#         return

#     print(n)
#     waqar(n-2)
# waqar(n)


# def sum_natural(n):
#     if n == 1:          # base case
#         return 1
#     else:
#         return n + sum_natural(n - 1)

# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers is:", sum_natural(n))


# def question1():
#     customer_ids = ["c101", "c102", "c103", "c104"]
#     for customer_id in customer_ids:
#         print(f"Processing customer ID: {customer_id}")
# question1()

# def question2():
#     customer_ids = ["c101", "c102", "c103", "c104"]
#     for i in customer_ids:
#         print(f"Dear {i}, your data has been processed successfully.")
# question2()

# def question3():
#     servers = [
#         {"name": "Server1", "location": "US-East", "status": "active"},
#         {"name": "Server2", "location": "US-West", "status": "inactive"},
#     ]

#     for server in servers:
#         print(f"{server['name']} is located in {server['location']} and is currently {server['status']}.")
# question3()

# def question4():
#     config1 = {"batch_size": 100}
#     config2 = {"timeout": 300}
#     config3 = {"retries": 5}
#     final_config = {}
#     final_config = {**config1, **config2, **config3}
#     # for config in [config1, config2, config3]:
#     #     final_config.update(config)
#     print(final_config)
# question4()





def question5():
    source1 = {'CPU': 30, 'Memory': 70}
    source2 = {'CPU': 40, 'Disk': 90}
    source = dict()
    distinct_keys = set(source1.keys()).union(set(source2.keys()))
    for key in distinct_keys:
        source[key] = source1.get(key, 0) + source2.get(key, 0)

    print(source)
question5()