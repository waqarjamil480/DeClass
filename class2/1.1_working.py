import  requests
# dummy data api for testing
response =requests.get('https://dummyjson.com/carts')
# 200 means successful response
# 404 means not found
response.status_code
response.headers
response.content
type(response.content)
type(response.json())


if response:
    if response.status_code == 200:
       content = response.json()
       print(content['carts'][0]['products'])
    else:
        print("Error: ", response.status_code)
       
else:
    print("Error: Response is None")

