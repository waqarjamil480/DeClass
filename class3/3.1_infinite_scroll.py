import requests
import json

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8',
    'priority': 'u=1, i',
    'referer': 'https://quotes.toscrape.com/scroll',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

i = 1

quotes = []

len(quotes[0])

while True:

    params = {
        'page': f'{i}',
    }
    print(f'page = {i}')

    response = requests.get('https://quotes.toscrape.com/api/quotes', params=params, headers=headers)

    quotes_li = response.json()
    
    quotes.append(quotes_li['quotes'])

    if quotes_li['has_next']:
        i = i + 1
    else:
        break

with open('quotes.json', 'w') as f:
    json.dump(obj=quotes, fp=f)

len(quotes)