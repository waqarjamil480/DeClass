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