from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
#localhost:5000/add/5/10
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'The sum of {num1} and {num2} is: {result}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  





