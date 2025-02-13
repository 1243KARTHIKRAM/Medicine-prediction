import pymongo
from flask import request

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
userdb = client['userdb']
users = userdb.customers

def insert_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']

        reg_user = {
            "name": name,
            "email": email,
            "password": password
        }

        # Check if user already exists
        if users.find_one({"email": email}) is None:
            users.insert_one(reg_user)
            return True
        else:
            return False

def check_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        user_data = users.find_one({"email": email, "password": password})

        if user_data is None:
            return False, ""
        else:
            return True, user_data["name"]
