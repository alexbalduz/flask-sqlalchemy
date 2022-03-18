from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World 2"

@app.route('/new')
def add_contact():
    return "saving a contact"