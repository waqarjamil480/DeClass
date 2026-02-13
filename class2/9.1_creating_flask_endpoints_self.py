from flask import Flask
app = Flask(__name__)

# this is just normal routing like localhost:5000/, localhost:5000/page
@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/page')
def page():
    return "This is the page!"

@app.route('/blog', methods=['GET'] )
def blog():
    return "this is the blog page"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)    






