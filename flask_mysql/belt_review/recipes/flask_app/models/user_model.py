import imp
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Email, Text_Field
from flask_app.models import recipe_model

class User:
    db = "recipes_schema" # Schema name here

    def __init__(self, data): # layout instance attributes according to table column header
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
    

############# Class Methods for interacting with the database #############

#---------------------------------
# ----------------------------------- Get All Users
# --------------------------------

    @classmethod 
    def get_all_users(cls):
        query =  "SELECT * FROM users;"
        returnedData = MySQLConnection(cls.db).query_db(query)
        user_instances = [cls(row) for row in returnedData]
        return user_instances

#---------------------------------
# ----------------------------------- Get User
# --------------------------------

    @classmethod 
    def get_user(cls, data):
        query =  """SELECT * FROM users 
                    LEFT JOIN recipes
                    ON users.id = recipes.users_id
                    WHERE users.id = %(id)s;"""
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        print(f"\n{returnedData}\n")
        user_instance = cls(returnedData[0])
        
        for row in returnedData:
            if row['recipes.id']:
                data = {
                    "id" : row['recipes.id'],
                    "users_id" : row["id"],
                    "name" : row['name'],
                    "description" : row['description'],
                    "instructions" : row['instructions'],
                    "made_on" : row['made_on'],
                    "less_than_30" : row['less_than_30'],
                    "created_at" : row['recipes.created_at'],
                    "updated_at" : row['recipes.updated_at']
                }
                user_instance.recipes.append(recipe_model.Recipe(data))

        return user_instance

#---------------------------------
# ----------------------------------- Add User
# --------------------------------

    @classmethod 
    def add_user(cls, data):
        query =  """INSERT INTO users (
                        first_name, last_name, email, password, created_at
                    )
                    VALUES(
                        %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());
                    """
        returned = MySQLConnection(cls.db).query_db(query, data)
        return returned

#---------------------------------
# ----------------------------------- Get User by Email
# --------------------------------

    @classmethod 
    def get_user_by_email(cls, data):
        print(data)
        query =  "SELECT * FROM users WHERE email = %(email)s;"
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        if len(returnedData) < 1:
            return False
        user_instance = cls(returnedData[0])
        return user_instance

#####################################################
############# Static Methods as helpers #############
#####################################################

#---------------------------------
# ----------------------------------- Form Validation
# --------------------------------

    @staticmethod
    def validate_registration(data):
        valid_form = True
        name = Text_Field(2)
        if not Email.inspect(data['email']):
            flash('Invalid Email address!')
            valid_form = False
        else:
            user = User.get_user_by_email(data)
            if user:
                flash('Email already in database!')
                return False
            
        if not name.inspect(data['first_name']):
            flash("First name must be at least 2 characters!")
            valid_form = False

        if not name.inspect(data['last_name']):
            flash("Last name must be at least 2 characters!")
            valid_form = False

        if data['password'] != data['confirm_password']:
            flash("Passwords must match!")
            valid_form = False

        return valid_form

#---------------------------------
# ----------------------------------- Login Validation
# --------------------------------

    @staticmethod
    def validate_login(data):

        if not Email.inspect(data['email']): # Check is email is valid with RegEx
            flash('Invalid Email address!')
            return False
        else:   # Check if email and password match a registered user
            return User.get_user_by_email(data) #search user by submitted email address
            