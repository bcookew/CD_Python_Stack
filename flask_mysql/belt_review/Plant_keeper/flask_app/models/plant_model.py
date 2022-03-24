from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Text_Field
from flask_app.models import user_model, user_plant_model
#################### Plant Model ####################

class Plant:
    db = "plant_keeper_schema" # Schema name here

    def __init__(self, data): # layout instance attributes according to table column header
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#----------------------------------
#-------------------------------------  Get plant by name
#----------------------------------

    @classmethod
    def get_plant_by_name(cls, data):
        query =  """SELECT *
                    FROM plants
                    WHERE
                    name = %(name)s"""
        returned_data = MySQLConnection(cls.db).query_db(query,data)
        if len(returned_data) < 1:
            return False
        data_stripped = returned_data[0]
        
        return cls(returned_data[0])

#----------------------------------
#-------------------------------------  Add new plant
#----------------------------------

    @classmethod
    def add_plant(cls, data):
        query =  """INSERT INTO
                    plants (name, created_at)
                    VALUES
                    (%(name)s, NOW())"""
        plant_id = MySQLConnection(cls.db).query_db(query,data)
        print(f'\nPlant {plant_id} Added!\n')
        return plant_id

    #----------------------------------
    #-------------------------------------  Add Ownership relationship
    #----------------------------------
    
    @classmethod
    def add_ownership(cls, data):
        query =  """INSERT INTO
            users_has_plants (users_id, plants_id, water_schedule, description)
            VALUES
            (%(users_id)s, %(plants_id)s);"""
        
        MySQLConnection(cls.db).query_db(query,data)
        print('\nPlant Ownership Established!\n')


    ####################  Helper Methods  ####################

    #----------------------------------
    #-------------------------------------  Validates new plant form fields
    #----------------------------------

    @staticmethod
    def validate_form(data):
        valid_form = True
        if not Text_Field(3,45).inspect(data['name']):
            flash('Plant name must be between 3-45 characters')
            valid_form = False
        if not Text_Field(10,500).inspect(data['name']):
            flash('Plant name must be between 10-500 characters')
            valid_form = False
        return valid_form

#----------------------------------
#-------------------------------------  Executes logic for add plant / relationship to owner
#----------------------------------

    @staticmethod        
    def add_new_plant(data):
        plant = Plant.get_plant_by_name(data)
        if not plant:
            plant_id = Plant.add_plant(data)
            relational_data = {
                "plants_id" : plant_id,
                "users_id" : data["user_id"]
            }
            Plant.add_ownership(relational_data)
        else:
            relational_data = {
                "plants_id" : plant.id,
                "users_id" : data["user_id"]
            }
            Plant.add_ownership(relational_data)


