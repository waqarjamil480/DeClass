from flask import Flask, render_template
import requests,json
app = Flask(__name__)
@app.route('/', methods=['GET'])

# http://localhost:5000/
def recipe_app():
    response = requests.get('https://dummyjson.com/recipes')
    data = response.json()['recipes']
    return render_template('recipes.html', recipes=data)



# http://localhost:5000/recipe
@app.route('/recipe', methods=['GET'])
def recipe_details():
    with open('recipes.json', 'r') as f:
        data = json.load(fp=f)
        recipes = data['recipes']
    return render_template('recipes.html', recipes=recipes)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)



