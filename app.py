from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #telling sqlalchemy the loccation of database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'sudheer'
api = Api(app)

jwt = JWT(app, authenticate, identity)

#items = []  #not needed, replaced by database

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')
#only the file you run is __main__
if __name__ == '__main__': #this is important because app.run will also execute when we are importing app.py in other file which we don't want
    from db import db # db initialized here to avoid problem of circular import
    db.init_app(app) 
    app.run(debug=True)  # important to mention debug=True