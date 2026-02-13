from flask import Flask
app = Flask(__name__)

#http://localhost:5000/house/12

@app.route('/house/<int:house_number>')
def house(house_number):
    return f'house number is: {house_number}'


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= 5000, debug=True)

