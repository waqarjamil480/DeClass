import requests
from bs4 import BeautifulSoup

# Fetch the page
url = "https://quotes.toscrape.com/tableful/"
response = requests.get(url)
response.raise_for_status()

# Parse TVB BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# The page is rendered oddly, but each quote appears in plain text lines:
texts = soup.get_text(separator="\n").splitlines()

clean_text = lambda text: text != ''

clean_text_space = lambda text: text.strip()

text = list(map(clean_text_space, texts))

text = list(filter(clean_text, text))


quotes = []

for index, line in enumerate(text):
    line = line.strip()
    if not line:
        continue
    # Detect lines that include quotes, authors, or tags
    if line.startswith('“') and '” Author:' in line:
        # Extract quote text and author
        quote_text, rest = line.split('”', 1)
        quote_text += '”'
        author = rest.split('Author:')[1].strip()
        quotes.append({'quote': quote_text, 'author': author})
    elif line.startswith('Tags:'):
        # Extract tags (followed from previous quote)
        
        for i in range(index, len(text)):
            if text[i].startswith('“'):
                quotes[-1]['tags'] = text[index+1:i]
                break

# Display the results
for q in quotes:
    print(q)
