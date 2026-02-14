import requests
from bs4 import BeautifulSoup

def get_random_quote():
    r = requests.get("https://quotes.toscrape.com/random")
    soup = BeautifulSoup(r.text, "html.parser")
    return {
        "text": soup.select_one("div.quote span.text").get_text(),
        "author": soup.select_one("div.quote small.author").get_text(),
        "tags": [t.get_text() for t in soup.select("div.quote div.tags a.tag")]
    }

# Example: Get 5 random quotes
quotes = [get_random_quote() for _ in range(5)]
for q in quotes:
    print(f"{q['text']} — {q['author']} ({', '.join(q['tags'])})")
