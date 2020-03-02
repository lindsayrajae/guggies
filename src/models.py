from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Nurses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(120))
    age=db.Column(db.String(120))
    work_exprience=db.Column(db.String(120))
    License=db.Column(db.String(120))
    years_working=db.Column(db.String(120))
    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "fullname": self.fullname,
            "username": self.username,
            "email": self.email,
            "password":self.password,
            "age": self.age,
            "work_exprience": self.work_exprience,
            "License": self.License,
            "years_working":self.years_working
        }