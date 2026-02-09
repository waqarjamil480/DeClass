import requests, os
from dotenv import load_dotenv

# this loads the .env file in your python scripts and you can use the VARIABLES inside it.
load_dotenv()

# here we are accessing the variable from .env file
api_key = os.getenv("GIT_API_KEY")

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = '{"description":"This is your updated repo!"}'

response = requests.patch('https://api.github.com/repos/zainkhangithub/Hello-World', headers=headers, data=data)

response.status_code

response.content