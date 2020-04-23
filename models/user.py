import sqlite3
from db import db

class UserModel(db.Model):
    
    #tell sqlalchemy the table name where models are stored
    __tablename__ = 'users'
    #id auto increments
    id = db.Column(db.Integer, primary_key = True) #primary_key means id is unique
    username = db.Column(db.String(90))
    password = db.Column(db.String(90))

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    #username mapping
    @classmethod
    def find_by_username(cls,_username):
        return cls.query.filter_by(username = _username).first()

    #userid mapping 
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by( id = _id ).first()
