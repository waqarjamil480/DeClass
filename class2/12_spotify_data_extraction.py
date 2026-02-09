import requests
import json

# get artist albums

artist_id = '3cKNppGLfcxdt9CtoHEZmQ'

url = f'https://api.spotify.com/v1/me'
headers = {"Authorization": f"Bearer BQDqf00obllt6eTY9M6xglc9aEpSl5YvicjGHXZeMvVh6x_jUtvJZjWo6JzIf3_xmdTpr15JGocpk_eP8jbETSK5Dzr7IUjWhVFrt_FzgAum_kfu0fxCglbMoFUAE1YylX-5Z4_XtxHJbps9MStlJUFIeOkUWDfsAwrut5AZiy0AKLmteW007rPdX8y5nh4-u7a9PUC20L9hLJ1WlRrYt4Ft9amd478vtw1nF2MSToSdtf9MQiS_GI3NPTi5Sw"}
response = requests.get(url, headers=headers)
data = response.json()
# open('albums.json', 'w').write(json.dumps(data, indent=4))
print(data)