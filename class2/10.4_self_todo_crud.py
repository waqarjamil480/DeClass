# /to/api/v1/  list all todos
# /to/api/v1/<id> -- get list of a todo by id
# /to/api/v1/create  -- create a new todo
# /to/api/v1/delete<id> -- delete a todo by id
# /to/api/v1/update<id> -- update a todo by id
from urllib import response
from flask import Flask, render_template, jsonify, request
import json, requests
app = Flask(__name__)

""" {
  "todos": [
    {
      "id": 1,
      "todo": "Do something nice for someone you care about",
      "completed": false,
      "userId": 152
    },
    {
      "id": 2,
      "todo": "Memorize a poem",
      "completed": true,
      "userId": 13
    },
  ],
  "total": 254,
  "skip": 0,
  "limit": 30
} """




@app.route('/todo/api/v1/', methods=['GET'])
def todo_all_list():
    response = requests.get('https://dummyjson.com/todos')
    code = response.status_code
    if code == 200:
        todos = response.json()['todos']
        return render_template('todo_list.html', todos=todos)
    else:
        error = f"Error: API returned status code {code}"
        return render_template('todo_list.html', error=error)
    
# @app.route('/todo/api/v1/', defaults={'id': 1, 'id2': 5}, methods=['GET'])
@app.route('/todo/api/v1/<int:id>/<int:id2>', methods=['GET'])
def todo_list(id, id2):
    response = requests.get('https://dummyjson.com/todos')
    code = response.status_code
    if code == 200: 
        if id >= 1 and id2 >= 1:
            id = id -1
            id2 = id2 -0
            todos = response.json()['todos'][id:id2]
            return render_template('todo_list.html', todos=todos)
        else: 
            error = f"Error: Invalid ID {id}. ID must be a positive integer."
            return render_template('todo_list.html', error=error)
    else:
        error = f"Error: API returned status code {code}"
        return render_template('todo_list.html', error=error)




 #/to/api/v1/create  -- create a new todo


#localhost:5000/todo/api/v1/create?id=31&todo=hellow&status=true
@app.route('/todo/api/v1/create', methods=['GET'])
def create_todo():
    response = requests.get('https://dummyjson.com/todos')
    code = response.status_code
    if code == 200: 

      all_data = response.json()['todos']
      new_todo={
          'id': request.args.get('id', 30), 
          'todo': request.args.get('todo', 'default todo - please provide todo text in url query parameter'), 
          'completed': request.args.get('status', False)
      }
      all_data.append(new_todo)
      return render_template('todo_list.html', todos=all_data)
  
    else:
        error = f"Error: API returned status code {code}"
        return render_template('todo_list.html', error=error)

if __name__ =='__main__':
    app.run(host = '0.0.0.0', port = '5000', debug= True)






