from models.user import UserModel #importing User class from user.py file we created

#OLD METHOD
#Create a list which acts as databse
#Create 2 mappings i.e uname->user , uid->user
"""
users = [  User(1,'bob','abcd')  ] #users is a list of User objects
username_mapping = { u.username : u  for u in users }
userid_mapping = { u.id : u  for u in users }
"""

#NEW METHOD
#Create database and create new functions in User class which do the work of mapping
def authenticate(username,password): 
    user = UserModel.find_by_username(username) 
    if user and user.password == password:
        return user #return that matched object and a JWT token


def identity(payload):#payload is the contents of the JWT token ,we extract the userid from that payload
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

