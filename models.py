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
    
class Elements(db.Model):

    atomicnum = db.Column(db.Integer, primary_key=True)
    symbol =  db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable = False)

    def __init__(self, atomicnum, symbol, name,imagename):
        self.atomicnum = atomicnum
        self.symbol = symbol
        self.name = name
        self.image = "{{url_for('static', filename='styles/"+ imagename+"')}}"
    
    def __repr__(self):
        return {
            "num": self.atomicnum,
            "symbol": self.symbol,
            "name": self.name,
            "imagelink": self.image
        }
        