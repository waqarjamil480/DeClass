from bs4 import BeautifulSoup
import requests

url = 'https://defang.io/#pricing'

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')