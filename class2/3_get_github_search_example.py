import requests

params = {
    'q': 'python api',      # search keywords
    'per_page': 10,          # limit results to 10
    'page': 1,
    'sort': 'updated'
}

url = 'https://api.github.com/search/repositories'

response = requests.get(url=url, params=params)
# Print the full response in text (JSON string)

response.text
print(response.text)