from app import app
from db import db

db.init_app(app)

@app.before_first_request #runs the method below it before the first request into the app
def create_tables():
    db.create_all() 

