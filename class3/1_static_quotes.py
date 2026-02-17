import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

# getting status codes
response.status_code



soup = BeautifulSoup(response.text, 'html.parser')
type(soup)
print(soup.prettify())
soup.select_one('h1 a').text

quote= soup.select_one('.quote')

soup.select_one('.text').text
soup.select_one('.author').text
