import requests, os
from dotenv import load_dotenv

# this loads the .env file in your python scripts and you can use the VARIABLES inside it.
load_dotenv("class2/.env", override=True)

# here we are accessing the variable from .env file
api_key = os.getenv("TOKEN")

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = '''{
        "name": "Hello-World2",
        "description": "This is your first repo!",
        "homepage": "https://github.com",
        "private": false,
        "is_template": true
    }'''

response = requests.post(
    'https://api.github.com/user/repos', 
    headers=headers, 
    data=data
)
response.status_code







