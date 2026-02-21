# pip install bs4
import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://www.marham.pk/labs/chughtai-lab'
path = ''

quotes = []

len(quotes)

while True:
    url = base_url + path

    print(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    quote_li = soup.select('#displayData data-labtestid')

    for quote in quote_li:

        quote_text = quote.select_one('p.test-name').text

        quote_author = quote.select_one('p.test-current-price').text

        tags = []

        quote_tags = quote.select('.tag')

        # for tag in quote_tags:
        #     tags.append(tag.text)

        # quotes.append({
        #     'quote_text': quote_text,
        #     'author': quote_author,
        #     'tags': tags
        # })

    if soup.select('.next'):
        path = soup.select_one('.next a')['href']
    else:
        break


    # print (path)
    # print(len(quotes_li))