import requests, os, json
from dotenv import load_dotenv
load_dotenv("class2/.env", override=True)
api_key1 = os.getenv('TOKEN')

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key1}',
    'X-GitHub-Api-Version': '2022-11-28',
}

response = requests.get('https://api.github.com/repos/waqarjamil480/Data_test/issues/1', headers=headers)
response.url
content =response.json()
print(json.dumps(content, indent=4))
# for key, value in content.items():
#     print(f"{key}: {value}")
