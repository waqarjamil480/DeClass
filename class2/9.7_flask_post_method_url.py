from flask import Flask,request

app = Flask(__name__)

@app.route('/mypost', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':  # to check this open postman and select post method send request + with data json
        data = request.get_json()      
        print(data)
        return 'This is a POST request', 200
    else:
        return 'This is a GET request'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)