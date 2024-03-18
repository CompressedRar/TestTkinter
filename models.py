from flask import *
from flask_sqlalchemy import *

db = SQLAlchemy()

class Students(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    confirmpassword = db.Column(db.String(100), nullable=False)

    def __init__(self, firstnm, password, confirmpass):
        
        self.firstname = firstnm
        self.password = password
        self.confirmpassword = confirmpass
    def __repr__(self):
        return {
             "firstname": self.firstname,
             "password": self.password}