import json, requests
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer',
    'X-GitHub-Api-Version': '2022-11-28',
}
# this repo is public that why we can see this even without token   Bearer <YOUR-TOKEN>
response = requests.get('https://api.github.com/repos/waqarjamil480/Data_test', headers)
response.status_code
raw_data = response.json()
response.text
type(response.text)


if response.status_code == 200:
    print('\n\n>>>>>>>The Data<<<<<<<\n\n')
    # for key, value in raw_data.items():
    #      print(f'{key} : {value}\n\n')
    # for data in raw_data:
    data=raw_data
    print(f'Name :{data['name']}\nemail : {data['owner']['login']}\nRepo Url : {data['owner']['url']}\n\n')


    
