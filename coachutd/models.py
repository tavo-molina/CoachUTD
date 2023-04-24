from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    about = db.Column(db.Text)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(100))
    availability = db.Column(db.String(100))

