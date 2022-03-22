from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Email, Password, Text_Field
from flask_app.models import user_model


class Course:
    db = "teachers_classes_students"
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.students = []
    
    ##############################
    ################################# Courses without specific user
    ##############################

    @classmethod
    def get_courses_without_user(cls,data):
        query =  """Select *
                    From classes
                    WHERE classes.id 
                    NOT IN (
                        SELECT classes_id FROM students_has_classes
                        LEFT JOIN students
                        ON students.id = students_has_classes.students_id
                        WHERE
                        students.id = %(id)s
                    );"""
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        courses = [cls(row) for row in returnedData]
        return courses

    ##############################
    ################################# Course with students
    ##############################
    
    @classmethod
    def get_course_with_students(cls,data):
        query =  """Select *
                    From classes
                    LEFT JOIN students_has_classes
                    ON students_has_classes.classes_id = classes.id
                    LEFT JOIN students
                    ON students.id = students_has_classes.students_id
                    WHERE 
                    classes.id = %(classes_id)s"""
        returnedData = MySQLConnection(cls.db).query_db(query,data)
        course = cls(returnedData[0])
        for row in returnedData:
            student = {
                "id" : row['students.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            course.students.append(user_model.User(student))
        return course
