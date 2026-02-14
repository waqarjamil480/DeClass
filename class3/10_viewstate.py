import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = "https://quotes.toscrape.com/search.aspx"

# STEP 1: Load the initial page to get __VIEWSTATE
r1 = session.get(url)
soup1 = BeautifulSoup(r1.text, "html.parser")
viewstate = soup1.find("input", {"name": "__VIEWSTATE"})["value"]

# STEP 2: Simulate selecting an author (e.g., "Albert Einstein")
payload1 = {
    "__VIEWSTATE": viewstate,
    "author": "Albert Einstein",
    "tag": "----------"
    # include other necessary form data like __EVENTTARGET, __EVENTARGUMENT if needed
}
url2 = 'https://quotes.toscrape.com/filter.aspx'
r2 = session.post(url2, data=payload1)
soup2 = BeautifulSoup(r2.text, "html.parser")
viewstate2 = soup2.find("input", {"name": "__VIEWSTATE"})["value"]

# STEP 3: Submit final search with chosen tag (e.g., "learning")
payload2 = {
    "__VIEWSTATE": viewstate2,
    "author": "Albert Einstein",
    "tag": "learning",
    # add form action, submit button name/value if required
}
r3 = session.post(url2, data=payload2)
soup3 = BeautifulSoup(r3.text, "html.parser")

# STEP 4: Extract quotes
for q in soup3.select(".quote"):
    text = q.select_one(".content").text
    author = q.select_one(".author").text
    tag = q.select_one(".tag").text
    print(f"{text} — {author} [{tag}]")
