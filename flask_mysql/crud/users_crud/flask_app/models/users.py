from msilib.schema import Class
from flask_app.config.mysqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users ORDER BY last_name'
        returned = MySQLConnection("users_schema").query_db(query)
        return returned

    @classmethod
    def insert(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW());'
        returned = MySQLConnection("users_schema").query_db(query,data)
        return returned

    @classmethod
    def pullByID(cls, id):
        data = {
            "id":id
        }
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        returned = MySQLConnection("users_schema").query_db(query, data)
        print("Returned:\n",returned,"\n")
        return returned[0]

    @classmethod
    def updateUser(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return MySQLConnection("users_schema").query_db(query,data)
        
    @classmethod
    def deleteUser(cls, id):
        
        data = {
            "id":id
        }
        query = "DELETE FROM users WHERE id = %(id)s"
        return MySQLConnection("users_schema").query_db(query,data)