from flask import Flask, request, redirect, render_template
import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://127.0.0.1:5000/callback'
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_API_TOKEN_URL = 'https://accounts.spotify.com/api/token'

@app.route('/')
def main():
    return render_template('spotify_welcome.html')

@app.route('/authorize')
def login():
    scope = 'user-read-private user-read-email'

    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': 'abcd'
    }
    # 'response_type=code&client_id=1467586874&scope='
    params_string = '&'.join([f"{k}={v}" for k,v in params.items()])
    auth_url = f'{SPOTIFY_AUTH_URL}?{params_string}'
    print(auth_url)
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    print(code)
    basic_auth = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
    auth_options = {
        'url': SPOTIFY_API_TOKEN_URL,
        'data': {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
        },
        'headers': {
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {basic_auth}'
        },
        'json': True
    }

    # # Make the POST request to Spotify's token endpoint
    response = requests.post(
        auth_options['url'],
        data=auth_options['data'],
        headers=auth_options['headers']
    )

    # # Handle the response
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        refresh_token = token_data['refresh_token']
        
    #     # You can now use the access_token to make API requests
        return f"Access Token: {access_token}, Refresh Token: {refresh_token}"
    else:
        return f"Error: {response.status_code}, {response.text}"
    # return code
app.run(port=5000)