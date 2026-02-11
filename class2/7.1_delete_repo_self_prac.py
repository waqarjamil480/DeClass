import requests,os
from dotenv import load_dotenv
load_dotenv("class2/.env", override=True)
api_key = os.getenv("TOKEN")

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
}
delete_repo_name ="Hello-World2"
owner_name = "waqarjamil480"
response = requests.delete(f'https://api.github.com/repos/{owner_name}/{delete_repo_name}', headers=headers)  
if response.status_code == 204:
    print("✅ Repository deleted successfully.")
elif response.status_code == 404:
    print("❌ Repository is not available or does not exist.")
elif response.status_code == 401:
    print("❌ Bad credentials.")
elif response.status_code == 403:
    print("❌ Permission denied. You may not have access.")
