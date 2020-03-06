"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import utils
# '''when am ready to compare the user password to user password i have to use hashlid(sha256) e.g pass = utils,sha256(json['password']
# we never store user passowrd we store it in the hashlib(sha256) and we get a random key which we compare it to what ever the user enter and if that matches the keyits good 
# ''''
import seeds
from flask import Flask, request, jsonify, url_for, render_template
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS

from utils import APIException, generate_sitemap
from models import db, Nurses,Userpatient,Userpatientprofile,Payment

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
# JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
# @app.route('/')
# def sitemap():
#     return generate_sitemap(app)

# @app.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "hello": "world"
#     }

#     return jsonify(response_body), 200

@app.route('/')
@app.route('/index', methods=['GET'])
def home():

<<<<<<< HEAD
    return render_template('layouts/homepage.html', title="zion")

@app.route('/userlogin')
def userlogin():

    return render_template('layouts/loginlayout')

@app.route('/nurselogin')
def nurselogin():

    return render_template('layouts/nurseloginlayout')

@app.route('/userprofile')
def userprofile():

    return render_template('layouts/user_profile.html')
=======
    return render_template('index.html')
>>>>>>> 56c6e3e4a7d5777ad75852ffd89dcf672731ae35

@app.route('/about')
def about():

    return render_template('layouts/about.html')

@app.route('/contact')
def contact():

    return render_template('layouts/contact.html')


@app.route('/nurses',methods=['POST'])
def add_nurse():
    nurse=request.get_json()
    nurses=Nurses(
        fullname=nurse['fullname'],
        username=nurse['username'],
        email=nurse['email'],
        password=nurse['password'],
        age=nurse['age'],
        work_exprience=nurse['work_exprience'],
        license=nurse['license'],
        years_working=nurse['years_working']
    )
    db.session.add(nurses)
    db.session.commit()
    return 'Nurse added successfully'
@app.route('/nurse_login',methods=['POST'])
def nurse_login():
    # return jsonify( create_jwt(identity=['email']))
    json = request.get_json()
    user = Nurses.query.filter_by(
        email = json['email'],
        password = utils.sha256(json['password'])
     ).first()
    if user is None:
        return "sorry account not found please check spelling and try again or if your new creat an account and start earning"
    return "you have logged in succesfully ' click to view "


# everything below relate to user and the patient
    

@app.route('/Userpatient',methods=['POST'])
def add_patient_and_user():
    user_and_patient=request.get_json()
    user_patient=Userpatient(
        fullname=user_and_patient['fullname'],
        username=user_and_patient['username'],
        email=user_and_patient['email'],
        password=user_and_patient['password'],
        age=user_and_patient['age'],
        gender=user_and_patient['gender'],
        race=user_and_patient['race'],
        home_address=user_and_patient['home_address'],
        patient_condition=user_and_patient[ "patient_condition"],
        patient_allergies=user_and_patient["patient_allergies"],
        patient_name=user_and_patient["patient_name"],
        patient_medications=user_and_patient["patient_medications"],
        patient_age=user_and_patient["patient_age"],
        patient_gender=user_and_patient["patient_gender"],
        patient_race=user_and_patient["patient_race"]
    )
    db.session.add(user_patient)
    db.session.commit()
    return 'User and Patient added successfully'

@app.route('/login',methods=['POST'])
def login():
    # return jsonify( create_jwt(identity=['email']))
    json = request.get_json()
    user = Userpatient.query.filter_by(
        email = json['email'],
        password = utils.sha256(json['password'])
     ).first()
    if user is None:
        return "sorry account not found please check spelling and try again or   create an account to become a member "
    return "you have logged in succesfully"





@app.route('/Userpatientprofile',methods=['POST'])
def user_patient_profile():
    user_patient_profile=request.get_json()
    user_patient_profile=Userpatient(
        fullname=user_patient_profile['fullname'],
        username=user_patient_profile['username'],
        home_address=user_patient_profile['home_address'],
        patient_condition=user_patient_profile[ "patient_condition"],
        patient_allergies=user_patient_profile["patient_allergies"],
        patient_name=user_patient_profile["patient_name"],
        patient_medications=user_patient_profile["patient_medications"],
        patient_age=user_patient_profile["patient_age"],
        patient_gender=user_patient_profile["patient_gender"],
        patient_race=user_patient_profile["patient_race"]
    )
    db.session.add(user_patient_profile)
    db.session.commit()
    return 'Userproifile  was created successfully'


@app.route('/Payment',methods=['POST'])
def payment():
    Payment=request.get_json()
    payment=Payment(
           card_num= payment ["card_num"],
            card_cvv = payment["card_cvv"],
            card_exp= payment ["card_exp"],
           card_name= payment ["card_name"]
    )
    db.session.add(Payment)
    db.session.commit()



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
