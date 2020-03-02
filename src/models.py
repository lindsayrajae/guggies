from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Nurses(db.Model):
    __tablename__ = 'nurses'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(120))
    age=db.Column(db.String(120))
    work_exprience=db.Column(db.String(120))
    license=db.Column(db.String(120))
    years_working=db.Column(db.String(120))
    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id":self.id,
            "fullname": self.fullname,
            "username": self.username,
            "email": self.email,
            "password":self.password,
            "age": self.age,
            "work_exprience": self.work_exprience,
            "license": self.license,
            "years_working":self.years_working
            
        }
class Userpatient(db.Model):
    __tablename__="userpatient"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    gender=db.Column(db. String(120))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age=db.Column(db.String(120))
    race=db.Column(db.String(120))
    password=db.Column(db.String(120))
    patient_name=db.Column(db.String(120))
    patient_age=db.Column(db.String(120))
    patient_condition=db.Column(db.String(120))
    patient_allergies=db.Column(db.String(120))
    patient_medications=db.Column(db.String(120))
    patient_gender=db.Column(db.String(120))
    patient_race=db.Column(db.String(120))
    home_address=db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id":self.id,
            "fullname": self.fullname,
            "username": self.username,
            "email": self.email,
            "password":self.password,
            "age": self.age,
            "gender":self.gender,
            "race":self.race,
            "patient_condition": self.patient_condition,
            "home_address":self.home_address,
            "patient_allergies":self.patient_allergies,
            "patient_name":self.patient_name,
            "patient_medications":self.patient_medications,
            "patient_age":self.patient_age,
            "patient_gender":self.patient_gender,
            "patient_race":self.patient_race
        }