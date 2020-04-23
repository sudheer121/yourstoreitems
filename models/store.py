#import sqlite3
from db import db

class StoreModel(db.Model):
    
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(90))
    """ #creates item object for each item maching store id may consume lot of space
    items = db.relationship('ItemModel') #reverse connection 
    #Goes into ItemModel gets the relationship
    #items is a list of item objects ( one(store) to many(items) mapping)
    """

    items = db.relationship('ItemModel',lazy='dynamic')
    #now items is not a list of objects but self.items.all() is a query builder

    def __init__(self,name): 
        self.name = name
       
    def json(self):
        return {'name':self.name, 'items': [item.json() for item  in self.items.all()] }

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first() #does all the database work
    
    def save_to_db(self):
        db.session.add(self) #we are inserting object
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
  