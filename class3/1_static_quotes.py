import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

# getting status codes
response.status_code