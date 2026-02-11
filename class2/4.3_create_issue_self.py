import requests, os
from dotenv import load_dotenv

load_dotenv("class2/.env", override=True)
api_key = os.getenv("TOKEN").strip()

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {api_key}",
    "X-GitHub-Api-Version": "2022-11-28",
}

payload = {
    "title": "3 Found a bug",
    "body": "I'm having a problem with this.",
    "labels": ["bug"]
}

url = "https://api.github.com/repos/waqarjamil480/Data_test/issues"
response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)
