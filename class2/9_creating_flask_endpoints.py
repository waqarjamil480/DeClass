from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    # code to fetch data from database
    return "Hello world!"

@app.route('/page')
def page():
    return "My First page"

@app.route('/blog', methods=['GET'])
def get_blog():
    return 'this is our blog page'

def multiply(id):
    return id * 10

@app.route('/product/<int:product_id>')
def product_id(product_id):
    return f"This is product number {multiply(product_id)}"

@app.route('/product/<string:product_name>')
def product_name(product_name):
    return f"This product is {product_name}"

@app.route('/product_details')
def product_details():
    return jsonify({
        "product_id": 1,
        "product_name": "shampoo",
        "is_available": False,
    }), 200
    
@app.route('/product_details/api/v1/product_query')
def product_query():
    if request.args:
        return jsonify({
            "product_id": request.args['id'],
            "product_name": request.args['name'],
            "is_available": request.args['is_available'],
        }), 200
    else:
        return 'Please mention query parameters when sending request'


@app.route('/product_post', methods=['POST', 'GET'])
def product_post():
    if request.method == 'POST':
        data = request.get_json()
        # print(data['name'])
        # print(type(data))
        # store data into DB
        return data, 200
        # return jsonify(data), 200
    return "not suitable for Get requests", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
