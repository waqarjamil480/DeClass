import requests
from bs4 import BeautifulSoup

cookies = {
    'hcbqz2uq': '1d9irk30hgpk',
    'h9a7zbso': 'tav9v9nhamgj',
    '41uff2gm': 'pdqrtyhyjvhn',
    '_ga_PSTTLHKHPF': 'GS2.1.s1754740321$o1$g0$t1754740321$j60$l0$h0',
    '_ga': 'GA1.1.1116682846.1754740321',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'hcbqz2uq=1d9irk30hgpk; h9a7zbso=tav9v9nhamgj; 41uff2gm=pdqrtyhyjvhn; _ga_PSTTLHKHPF=GS2.1.s1754740321$o1$g0$t1754740321$j60$l0$h0; _ga=GA1.1.1116682846.1754740321',
}

response = requests.get('https://www.oicci.org/members-directory/', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

soup.select('.card-body')