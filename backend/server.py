from flask import Flask
from db import generate_schema

app = Flask(__name__)

@app.route('/schema/')
def get_schema():
    return generate_schema()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"