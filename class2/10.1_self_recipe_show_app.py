from flask import Flask, json, render_template
app = Flask(__name__)
@app.route('/')
def recipes_app():
    with open('recipes.json','r') as f:
        data = json.load(fp=f)
        recipes = data['recipes']
        total_recipes = data['total']
    return render_template('recipes2.html', recipes=recipes, total_recipes=total_recipes)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

