from flask import Flask, request
from flask_cors import CORS, cross_origin
from db import wrap_serialize, \
    get_user_max_by_weights, \
    get_personal_bests, get_id_given_name, get_workout_by_name, get_workout_by_user

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route('/schema/')
def get_schema():
    return generate_schema()

@cross_origin()
@app.route('/api/<table>/<_id>')
def get_obj(table, _id):
    return wrap_serialize(table, int(_id))

@cross_origin()
@app.route('/api/max_weights/')
def get_user_max():
    return get_user_max_by_weights()

@cross_origin()
@app.route('/api/personal_best/<_id>')
def get_personal_best(_id):
    return get_personal_bests(_id)

@cross_origin()
@app.route("/api/user_id")
def get_given_name():
    if request.method == 'GET':
        return get_id_given_name(request.args['name'])

@cross_origin()
@app.route("/api/get_workout_name")
def get_workout_name():
    if request.method == 'GET':
        return get_workout_by_name(request.args['user'], request.args['name'])

@cross_origin()
@app.route("/api/get_workout_user")
def get_workout_user():
    if request.method == 'GET':
        return get_workout_by_user(request.args['user'])

@cross_origin()
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"