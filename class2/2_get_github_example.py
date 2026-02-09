import requests, json

# sending an api request to the github server and receiving response for it
res = requests.get('https://api.github.com')

# extracting response status code and content and checking the content type
res.status_code
res.headers
res_content_in_bytes = res.content
type(res_content_in_bytes)

# converting content to string using decode and to python dictionary using json.loads()
github_data_dic = json.loads(res_content_in_bytes.decode('utf-8'))
type(github_data_dic)


# dumping githubt api data into a json file
with open('github_example.json', 'w') as f:
    json.dump(github_data_dic, fp=f)
