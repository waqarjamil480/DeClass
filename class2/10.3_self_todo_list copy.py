from flask import Flask, render_template
import json, requests
app = Flask(__name__)

#http://localhost:5000/
@app.route('/', methods=['GET'])
def todo_list():
    with open('todo_list.json', 'r') as f:
        data = json.load(fp=f)
        todos = data['todos']   
    return render_template('todo_list.html', todos=todos)



#http://localhost:5000/todos

@app.route('/todos', methods=['GET'])
def todo_list2():
    response = requests.get('https://dummyjson.com/todos')
    todos = response.json()['todos']
    return render_template('todo_list.html', todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
