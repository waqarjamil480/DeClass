def question1():
# You’ve received a small batch of customer data. customer_ids = ["c101", "c102", "c103", "c104"]
# Store the following customer IDs in a list and print each ID using indexing:
    customer_ids = ["c101", "c102", "c103", "c104"]
    for i in range(len(customer_ids)):
        print(customer_ids[i] + " index is:",i)
question1()


def question2():
# Using the customer_ids list, send a status message to each customer:
# Dear C101, your data has been processed successfully.
    customer_ids = ["c101", "c102", "c103", "c104"]
    for i in customer_ids:
        print(f"Dear {i}, your data has been processed successfully.")
question2()