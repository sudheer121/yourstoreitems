#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser() #class variable, we'll be using it in POST AND PUT request
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': 'Item not found'},404
     
    

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with name {} already exists".format(name)},400
        
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        print(item.json())
        try:
            item.save_to_db()
        except Exception as ex :
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print( message )
            return {"message":"An error!! occured while inserting the item"},500 #internal server error
        
        return item.json(),201
 
    

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}


    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()   
        return item.json()

    

class ItemList(Resource):
    def get(self):
        return { 'items': [item.json() for item in ItemModel.query.all()]}
        #.query.all() gives us a list of all the rows 