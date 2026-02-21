# pip install bs4
import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://quotes.toscrape.com'
path = ''

quotes_li = []

while True:
    url = base_url + path

    # print (path)
    # print(len(quotes_li))

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select('.quote')

    for quote in quotes:

        quote_text = quote.select_one('span.text').text
        author_name = quote.select_one('span small.author').text

        tags = quote.select('.tags .tag')

        tag_li = []

        for tag in tags:
            tag_li.append(tag.text)

        quote_data = {
            'quote': quote_text,
            'author_name': author_name,
            'tags': tag_li
        }
        
        quotes_li.append(quote_data)

        # print(f'Quote: {quote_text}')
        # print(f'Autho Name: {author_name}')
        # print(f'Tags: {tag_li}\n')
        # print(type(soup.select_one('li.next')))

        filepath = path.split('/')

        if path:
            filepath = filepath[2]
        else:
            filepath = '1'

        with open(f'E:\de\class\DeClass\class4\get_quotes\quotes\page_{filepath}.json', 'w') as f:
            json.dump(quote_data, f)

    if soup.select_one('li.next'):
        path = soup.select_one('li.next a')['href']
    else:
        break