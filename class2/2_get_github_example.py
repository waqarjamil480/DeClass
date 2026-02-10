import requests, json

# sending an api request to the github server and receiving response for it
res = requests.get('https://api.github.com')

# extracting response status code and content and checking the content type
res.status_code
res.headers
res_content_in_bytes = res.content
type(res.content)

# converting content to string using decode and to python dictionary using json.loads()
github_data_dic = json.loads(res_content_in_bytes.decode('utf-8'))
# need to as this
# content = res.json()
# type(content)
# if content == github_data_dic:
#     print('Both content and github_data_dic are same')
type(github_data_dic)


# dumping githubt api data into a json file
with open('github_example.json', 'w') as f:
    json.dump(github_data_dic, fp=f)


# done this my self ----reading json data from the file    
with open('github_example.json', 'r') as f:
    data_form_file = json.load(fp=f)
    #print(data_form_file.items())
    for key, value in data_form_file.items():
        print(key, " : ", value + "\n")
  
    # print(data_form_file)
    print(type(data_form_file))
