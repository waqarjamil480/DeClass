import requests, os, json
from dotenv import load_dotenv
# this loads the .env file in your python scripts and you can use the VARIABLES inside it.
load_dotenv()
 
# here we are accessing the variable from .env file
api_key = os.getenv('TOKEN')
# https://api.github.com/repos/OWNER/REPO

# Bearer <YOUR-TOKEN> remove <> and put key"
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
}

url = 'https://api.github.com/repos/waqarjamil480/Data_test'

response = requests.get(url=url, headers=headers)

response.status_code
response.content


with open('git_repo.json', 'w') as f:
    json.dump(response.json(), fp=f)