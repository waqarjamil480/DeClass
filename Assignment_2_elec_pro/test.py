import requests

# 1 Province Test
res1 = requests.get("http://localhost:5000/province?province=Punjab")
print("Province Test:", res1.status_code)

# 2 History Only Year
res2 = requests.get("http://localhost:5000/history?year=2013")
print("History Year Test:", res2.status_code)

# 3 History Year + Province
res3 = requests.get("http://localhost:5000/history?year=2018&province=Sindh")
print("History Year + Province:", res3.status_code)
