import  requests
# dummy data api for testing
response = requests.get('https://jsonplaceholder.typicode.com/users')
response.status_code
response.headers
response.content
type(response.content)
if response:
    if response.status_code == 200:
        content = response.json()
        main_data = content
        print(main_data)
        for data in main_data:
            data_format = 'ID = {}\n NAME = {}\n EMAIL = {} \n ADDRESS = {} \n'
            data_format = data_format.format(data['id'], data['name'], data['email'], data['address'])
            print(data_format)
