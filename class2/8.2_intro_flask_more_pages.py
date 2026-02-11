from flask import Flask
app = Flask(__name__)





@app.route('/')
def hello():
    return "This is 1st page"