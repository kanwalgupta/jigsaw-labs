from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/players')
def whatever():
    return 'first player, second player '

app.run(debug=True)

