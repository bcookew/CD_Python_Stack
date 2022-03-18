import re
from flask import flash
from flask_app.config import mysqlconnection





email_validator = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM emails;"
        returnedData = mysqlconnection.connectToMySQL("email_schema").query_db(query)
        instances = [cls(row) for row in returnedData]
        return instances

    @classmethod
    def addEmail(cls, data):
        query = "INSERT INTO emails (email, created_at) VALUES ( %(email)s, NOW() );"
        returnedData =  mysqlconnection.connectToMySQL("email_schema").query_db(query, data)
        if returnedData != None:
            flash("You successfully input an email address!")
        return returnedData

    @classmethod
    def validate(cls, data):
        form_valid = True
        comparison_data = cls.getAll()
        if not email_validator.match(data["email"]):
            flash("Invalid email address")
            form_valid = False
            return form_valid
        for inst in comparison_data:
            if inst.email == data['email']:
                flash("Email already in database")
                form_valid = False
                return form_valid
        return form_valid
