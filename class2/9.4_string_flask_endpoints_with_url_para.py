from flask import Flask
app= Flask(__name__)

@app.route('/<string:name1>/<string:name2>')
def welcome(name1, name2):
	return f'name1:{name1} and name2:{name2}'
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
