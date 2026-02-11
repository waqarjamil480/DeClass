import requests,os,json
from dotenv import load_dotenv
load_dotenv("class2/.env", override=True)
api_key = os.getenv("TOKEN")

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {api_key}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
}


# old_repo_name_to_update = "Hello-World"
# new_repo_name_to_update = "Test_Data_Eng_Repo"
old_repo_name_to_update = input("Enter the name of the repository you want to update: ")
new_repo_name_to_update = input("Enter the new name for the repository: ")
repo_owner = "waqarjamil480"


data = {
    "name":new_repo_name_to_update,
    "description":"This is your first repository",
    "homepage":"https://github.com",
    "has_issues":True,
    "has_projects":True,
    "has_wiki":True
}
# patch means update at here
response = requests.patch(f'https://api.github.com/repos/{repo_owner}/{old_repo_name_to_update}', headers=headers, json=data)


# ---------------- RESPONSE HANDLING ---------------- #

if response.status_code == 200:
    updated_data = response.json()
    print("\n✅ Repository Updated Successfully!\n")
    print(f"Old Name : {old_repo_name_to_update}")
    print(f"New Name : {updated_data['name']}")
    print(f"Repo URL : {updated_data['html_url']}")

elif response.status_code == 404:
    print(f"\n❌ Repository '{old_repo_name_to_update}' not found.")

elif response.status_code == 401:
    print("\n❌ Unauthorized! Check your API token.")

elif response.status_code == 422:
    print(f"\n❌ Repository name '{new_repo_name_to_update}' already exists or invalid.")

else:
    print("\n⚠ Unexpected Error")
    print(f"Status Code: {response.status_code}")
    print("Full Error Response:")
    print(json.dumps(response.json(), indent=4))