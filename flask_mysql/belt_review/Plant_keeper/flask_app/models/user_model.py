from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Email

class User:
    db = "plant_keeper_schema" # Schema name here

    def __init__(self, data): # layout instance attributes according to table column header
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

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
        query =  "SELECT * FROM users WHERE id = %(id)s;"
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        user_instance = cls(returnedData[0])
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
        
        if not Email.inspect(data['email']):
            flash('Invalid Email address!')
            valid_form = False
        else:
            user = User.get_user_by_email(data)
            if user:
                flash('Email already in database!')
                return False
            
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters!")
            valid_form = False

        if len(data['last_name']) < 2:
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
            