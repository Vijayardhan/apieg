from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "hrllo world"
@app.route("/about")
def about():
    return "hello about"