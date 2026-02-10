import requests, json

params = {
    'q': 'python api',      # search keywords
    'per_page': 10,          # limit results to 10
    'page': 1,
    'sort': 'updated'
}
# this is query parameters
    
url = 'https://api.github.com/search/repositories'

response = requests.get(url, params)

# Print the full response in text (JSON string)

# done this in class
response.text
data = response.json()
with open('git_search.json', 'w') as f:
    json.dump(data,f)
    print(response.text[1:20])

