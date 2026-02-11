import requests, os
from dotenv import load_dotenv
load_dotenv("class2/.env", override=True)
api_key = os.getenv("TOKEN")

create_repo_name = "Hello-World3"
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    "name": create_repo_name,
    "description": "This is your first repository",
    "homepage": "https://github.com",
    "private": False,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
}


# data = '{"name":"HELLO_3","description":"This is your first repository","homepage":"https://github.com","private":false,"has_issues":true,"has_projects":true,"has_wiki":true}'
# response = requests.post('https://api.github.com/user/repos', headers=headers, data=data)
response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)

if response.status_code == 201:
    print("✅ Repository created successfully!")

elif response.status_code == 422:
    print("⚠️ Repository already exists.")

elif response.status_code == 422 and "name already exists" in str(data):
    print("Repository already exists.")

elif response.status_code == 401:
    print("❌ Bad credentials. Check your token.")

else:
    print(f"❌ Failed. Status code: {response.status_code}")