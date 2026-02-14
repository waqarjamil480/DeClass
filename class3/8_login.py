import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://quotes.toscrape.com/login"
QUOTES_URL = "https://quotes.toscrape.com/"

session = requests.Session()

# 1. Get the login page to retrieve CSRF token
login_page = session.get(LOGIN_URL)
soup = BeautifulSoup(login_page.text, "html.parser")
csrf = soup.find("input", {"name": "csrf_token"})["value"]

# 2. Perform login
payload = {
    "username": "anyuser",
    "password": "anypass",
    "csrf_token": csrf
}
session.post(LOGIN_URL, data=payload)

# 3. Access a page now behind login walls
response = session.get(QUOTES_URL)
soup = BeautifulSoup(response.text, "html.parser")

for quote in soup.select(".quote"):
    text = quote.select_one(".text").get_text()
    author = quote.select_one(".author").get_text()
    print(f"{text} — {author}")
