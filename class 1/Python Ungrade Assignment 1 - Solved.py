def question1():
    customer_ids = ['C101', 'C102', 'C103', 'C104']
    print('Customer Id List:')

    for index in range(0, len(customer_ids)):
        print(customer_ids[index])

def question2():
    customer_ids = ['C101', 'C102', 'C103', 'C104']
    for customer_id in customer_ids:
        print(f'Dear {customer_id}, your data has been processed successfully')

def question3():
    servers = [
        {'name': 'Server1', 'location': 'US-East', 'status': 'active'},
        {'name': 'Server2', 'location': 'US-West', 'status': 'inactive'},
    ]

    for server in servers:
        print(f'{server['name']} is located in {server['location']} and is currently {server['status']}.')

def question4():
    config1 = {'batch_size': 100}
    config2 = {'timeout': 300}
    config3 = {'retries': 5}

    config = {**config1, **config2, **config3}

    print(config)

def question5():
    source1 = {'CPU': 30, 'Memory': 70}
    source2 = {'CPU': 40, 'Disk': 90}

    source = dict()

    distinct_keys = set(source1.keys()).union(set(source2.keys()))

    # print(distinct_keys)

    for key in distinct_keys:
        source[key] = source1.get(key, 0) + source2.get(key, 0)

    print(source)

def question6():
    emp_ids = ['E01', 'E02']
    names = ['Alice', 'Bob']
    departments = ['HR', 'IT']

    emp_data = [{emp_id: {'name': name, 'department': department}} for emp_id, name, department in zip(emp_ids, names, departments)]

    print(emp_data)


def question7():
    region_codes = {101: 'North', 102: 'South', 103: 'East'}

    list_of_list = [[k, v] for k, v in region_codes.items()]

    print(list_of_list)

def question8():
    usage = {'job1': 300, 'job2': 120, 'job3': 560, 'job4': 560, 'job5': 400}

    def top_n_jobs(n):
        li = sorted(usage.items(), key=lambda x: x[1], reverse=True)
        top_jobs = [item[0] for item in li][:n]
        print(top_jobs)

    top_n_jobs(3)

def question9():
    records = [
        {'id': 'A1', 'value': 100},
        {'id': 'A2'},
        {'value': 200},
        {'id': 'A3', 'value': 150}
    ]

    filtered_records = [record for record in records if 'id' in record and 'value' in record]
    print(filtered_records)

def question10():
    customer_ids = ['C101', 'C102', 'C103', 'C104']

    with open('pipeline_log.txt', 'w') as f:
        for customer_id in customer_ids:
            f.writelines(f'Processed customer: {customer_id}\n')

if __name__ == '__main__':
    # question1()
    # question2()
    # question3()
    # question4()
    # question5()
    # question6()
    # question7()
    question8()
    # question9()
    # question10()