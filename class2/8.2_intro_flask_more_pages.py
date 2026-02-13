from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'] )
def welcome():
    return "this is the index page"

@app.route('/about')
def aboutpage():
    return "this is the about page"

@app.route('/contact')
def contactpage():
    return "this is the contact page"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)