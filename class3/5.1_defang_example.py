from bs4 import BeautifulSoup
import requests

url = 'https://defang.io/pricing/'

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
soup.select_one('h3').text
soup.select_one('.mb-4 p.text-left').text
soup.select_one('p span.font-guaruja').text



all_boxes = soup.select('div div div div')


for boxes in all_boxes :
   print( boxes.select_one('h3').text)


