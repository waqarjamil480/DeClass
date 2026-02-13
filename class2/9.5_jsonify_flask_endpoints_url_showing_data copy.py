from flask import Flask, jsonify
app = Flask(__name__)
# http://localhost:5000/ac
@app.route('/ac', methods=['GET'])
def product_details():
	return jsonify({
		"product_name" : "Dawlance AC",
		"Product Quantity": 200,
		"Availability in Karachi": True,
		"Shipping charges": 1000
	}), 200
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port= 5000, debug=True)


