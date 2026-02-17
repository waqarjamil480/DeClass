from bs4 import BeautifulSoup
import requests

url = 'https://ploomber.io/pricing/'

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

pricing_items = soup.select('div.pricing-item')

pricing_li = []

for pricing_item in pricing_items:
    pricing_info = {
        'price_title' : pricing_item.select_one('.pricing-title').text,
        'price_value' : pricing_item.select_one('.price .price-value').text
    }
    pricing_li.append(pricing_info)