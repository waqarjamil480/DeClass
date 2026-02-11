from flask import Flask
#1 import Flask library and instance flask object from flask

#2 create an instance of the Flask class and assign it to the variable app If If you run file directly → __name__ = "__main__"
#  or   __name__ = filename  If imported
app = Flask(__name__)



# 2.1 define a route for the root URL ("/") and specify that it accepts GET requests. 
# When a GET request is made to the root URL, the welcome function will be executed, returning the
@app.route('/', methods=['GET'])

#2.2 define the welcome function that will be executed when a GET request is made to the root URL.
def welcome():
   return "Hello World!"


#3 check if the script is being run directly (not imported as a module) 
# If file is imported somewhere else → this will NOT run.
if __name__ == '__main__': 
#4 run the Flask application on localhost at port 5000
   app.run(host='localhost', port=5000)



