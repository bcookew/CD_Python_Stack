from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

email_validator = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

dojo_survey = connectToMySQL("dojo_survey_schema")

class Survey:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def submitSurvey(cls,data):
        query =  """INSERT INTO 
                    dojos (
                        name, email, location, language, comment, created_at)
                    VALUES (
                        %(name)s, %(email)s, %(location)s, %(language)s, %(comment)s, NOW());"""
        dojo_survey.query_db(query, data)

    @staticmethod
    def validate_fields(data):
        valid_form = True
        if len(data["name"]) < 3:
            flash("Name must be more than 3 characters")
            valid_form = False
        if not email_validator.match(data["email"]):
            flash("Input a valid eMail Address")
            valid_form = False
        return valid_form