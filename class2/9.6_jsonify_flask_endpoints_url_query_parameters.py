from flask import Flask, jsonify, request
# from markupsafe import escape


# app = Flask(__name__)
# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"


app = Flask(__name__)
@app.route('/product/details')
# if request.args  then to pass a pery parameter is must
# http://localhost:5000/product/details?id=12&name=product1&qty=12&available=True
# no.1 if removed then we can even use http://localhost:5000/product/details and it will give default values

# no.1
# def product_details():
#         pro_details={
#             "product_id": request.args.get('id', 12),
#             "product_name": request.args.get('name','ac'),
#             "product_quntity": request.args.get('qty', 100),
#             "product_availability": request.args.get('available', False),
#         }
#         return f"details are: {pro_details} and type {type(pro_details)}", 200


# http://localhost:5000/product/details?id=12
# no.2
# def product_details():
#     if request.args:
#         pro_details={
#             "product_id": request.args.get('id', 12),
#             "product_name": request.args.get('name','ac'),
#             "product_quntity": request.args.get('qty', 100),
#             "product_availability": request.args.get('available', False),
#         }
#         return f"details are: {pro_details} and type {type(pro_details)}", 200
#     else:
#         print('Please mention query parameters when sending request')
		

# http://localhost:5000/product/details?id=12&name=bottle
# this will return json response
def product_details():
    if not request.args:
        return jsonify({
            "error": "Missing query parameters",
            "message": "Please provide product details like ?id=1&name=abc&qty=10&available=true"
        }), 400   # 400 = Bad Request

    pro_details={
        "product_id": request.args.get('id', 12),
        "product_name": request.args.get('name','ac'),
        "product_quntity": request.args.get('qty', 100),
        "product_availability": request.args.get('available', False),
    }
    return jsonify(pro_details), 200


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port ='5000', debug=True)




