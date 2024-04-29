from flask import Flask
from db import generate_schema, wrap_serialize

app = Flask(__name__)

@app.route('/schema/')
def get_schema():
    return generate_schema()

@app.route('/api/<table>/<_id>')
def get_obj(table, _id):
    return wrap_serialize(table, int(_id))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"