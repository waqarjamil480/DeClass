from flask import Flask

# import library and instance flask object
app = Flask(__name__)

# api endpoint
@app.route('/', methods=['GET'])
def welcome():
   return "Hello World!"

if __name__ == '__main__':
   app.run(host='localhost', port=5000)
