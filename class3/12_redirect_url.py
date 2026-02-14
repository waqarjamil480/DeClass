from bs4 import BeautifulSoup
import requests

url = "https://example.com"
html = requests.get(url, allow_redirects=False).text
soup = BeautifulSoup(html, "html.parser")

links = []
for a in soup.find_all("a", href=True):
    style = a.get("style", "").lower()
    if "display:none" in style or "visibility:hidden" in style or "left:-" in style:
        continue  # Skip honeypot
    links.append(a["href"])

print(links)
