import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

# getting status codes
response.status_code

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

soup.select_one('h1 a').text

quotes = []

quote_li = soup.select('.quote')

for quote in quote_li:

    quote_text = quote.select_one('.text').text

    quote_author = quote.select_one('.author').text

    tags = []

    quote_tags = quote.select('.tag')

    for tag in quote_tags:
        tags.append(tag.text)

    quotes.append({
        'quote_text': quote_text,
        'author': quote_author,
        'tags': tags
    })

quote_dict = {
    'quotes': quotes
}

with open('quotes.json', 'w') as f:
    json.dump(obj=quote_dict, fp=f)