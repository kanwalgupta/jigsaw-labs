from flask import Flask, render_template
app = Flask(__name__, static_folder='public',template_folder = 'templates')

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/restaurants")
def restaurants():
    #return "<ul><li>chipotle, sweetgreen, and five guys</li></ul>"
    return render_template('restaurants.html')

@app.route("/restaurants/<name>")
def restaurant_name(name):
    #return f"<h1>Welcome to {name}</h1>"
    return render_template('restaurant_name.html', name=name) 