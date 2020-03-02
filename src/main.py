"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, render_template
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Nurses

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@app.route('/nurses',methods=['POST'])
def add_nurse():
    nurse=request.get_json
    nurses=nurse(
    fullname=nurse['fullname'],
    username=nurse['username'],
    email=nurse['email'],
    password=nurse['password'],
    age=nurse['age'],
    work_exprience=nurse['work_exprience'],
    license=nurse['License'],
    years_working=nurse['years_working']

    )
    db.session.add(nurses)
    db.session.commit()

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
