import requests, json
headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
}
api_url = 'https://api.github.com/search/users'
params = {
    'q': 'waqarjamil480',
}

response = requests.get(api_url, params)
response.headers
response.status_code
# print(response.url)
if response:
    if response.status_code == 200:
        print('\n>>>>>>show data<<<<<<<<')
        data_all = json.loads(response.content.decode('utf-8'))
        json_list = []
        
        for data in data_all['items']:
            data_dict = {
                "login Name": data['login'],
                "ID": data['id'],
                "URL": data['html_url']
            }
            json_list.append(data_dict)
            # here this logic will be wrong because this will add /n too in file so we use append with dict
            # format = 'login Name: {} ID: {} Url:{}'
            # format = format.format(data['login'], data['id'], data['html_url'])
            print(f'login Name: {data['login']}\nID: {data['id']}\nUrl:{data['html_url']}')
        print('>>>>>>data<<<<<<<<')
        # print(data_all)
        # type(data_all)
    with open('waqar_get_use_in_git_self.json', 'w') as f:
        json.dump(json_list, f)
        print('Added data in file "waqar_get_use_in_git_self.json"')