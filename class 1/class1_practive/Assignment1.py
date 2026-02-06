from xmlrpc import server


def question1():
# You’ve received a small batch of customer data. customer_ids = ["c101", "c102", "c103", "c104"]
# Store the following customer IDs in a list and print each ID using indexing:
    customer_ids = ["c101", "c102", "c103", "c104"]
    for i in range(len(customer_ids)):
        print(customer_ids[i] + " index is:",i)
# question1()


def question2():
# Using the customer_ids list, send a status message to each customer:
# Dear C101, your data has been processed successfully.
    customer_ids = ["c101", "c102", "c103", "c104"]
    for i in customer_ids:
        print(f"Dear {i}, your data has been processed successfully.")
# question2()

def question3():
    #Create a list of dictionaries, where each dictionary holds server details:
    # servers = [
    #     {"name": "Server1", "location": "US-East", "status": "active"},
    #     {"name": "Server2", "location": "US-West", "status": "inactive"},
    # ]
    # Print a message like: Server1 is located in US-East and is currently active.
    servers = [
        {"name": "Server1", "location": "US-East", "status": "active"},
        {"name": "Server2", "location": "US-West", "status": "inactive"},
    ]

    for server in servers:
        print(f"{server['name']} is located in {server['location']} and is currently {server['status']}.")

# question3()



def question4():
    config1 = {"batch_size": 100}
    config2 = {"timeout": 300}
    config3 = {"retries": 5}
    final_config = {}
    final_config = {**config1, **config2, **config3}
    # for config in [config1, config2, config3]:
    #     final_config.update(config)

    print(final_config)

# question4()



def question5():
    source1 = {'CPU': 30, 'Memory': 70}
    source2 = {'CPU': 40, 'Disk': 90}
    new = dict()
    all_sep_keys = set(source1.keys()).union(set(source2.keys()))

    for key in all_sep_keys:
         new[key] = source1.get(key, 0) + source2.get(key, 0)
    print(new)
# question5()


def question6():
    emp_ids = ['E01', 'E02']
    names = ['Alice', 'Bob']
    departments = ['HR', 'IT']
    result = [{emp_id: {'name': name, 'department': department}} 
            for emp_id, name, department in zip(emp_ids, names, departments)]
    print(result)
# question6()


def question7():
    region_codes = {101: 'North', 102: 'South', 103: 'East'}

    final_list = [[keys, value] for keys, value in region_codes.items()]

    print(final_list)
# question7()

def question8():
    usage = {'job1': 300, 'job2': 120, 'job3': 560, 'job4': 560, 'job5': 400}

    def required_jobs(n):
        li = sorted(usage.items(), key=lambda x: x[1], reverse=True)
        highjobs = [item[0] for item in li][:n]
        print(highjobs)

    required_jobs(3)



# question1()
# question2()
# question3()
# question4()
# question5()
# question6()
# question7()
question8()