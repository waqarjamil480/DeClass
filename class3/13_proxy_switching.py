import requests
import itertools

# Example list of proxies (IP:PORT format)
proxies_list = [
    # "http://188.42.89.255:80",
    # "http://63.141.128.86:80",
    # "http://104.27.4.49:80",
    # "http://185.162.230.222:80",
    "http://321.222.333.444:80"
]

# Cycle through proxies endlessly
proxy_cycle = itertools.cycle(proxies_list)

url = "https://httpbin.org/ip"

for i in range(5):  # make 5 requests
    proxy = next(proxy_cycle)
    proxies = {"http": proxy}
    print(proxies)
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        print(response.json())
    except requests.exceptions.RequestException:
        print(f"Proxy failed: {proxy}")
