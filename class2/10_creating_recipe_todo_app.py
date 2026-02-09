from flask import Flask, jsonify, request, render_template
import json, requests

app = Flask(__name__)

todos = []


@app.route('/recipes')
def show_recipes():
    response = requests.get('https://dummyjson.com/recipes')
    # with open('recipes.json', 'r') as f:
    #     data = json.load(fp=f)
    #     recipes = data['recipes']
    recipes = response.json()['recipes']
    return render_template("recipes.html", recipes=recipes)

@app.route('/todos')
def show_todos():
    # with open('todo.json', 'r') as f:
    #     data = json.load(fp=f)
    #     todos = data['todos']
    return render_template("todo_list.html", todos=todos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
