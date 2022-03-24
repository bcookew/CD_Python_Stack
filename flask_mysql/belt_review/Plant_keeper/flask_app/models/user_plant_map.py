from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Text_Field
from flask_app.models import user_model, plant_model

####################  User Plant Map Class  ####################

class User_Plant_Map:
    db = "plant_keeper_schema" # Schema name here

    def __init__(self, map_data): # layout instance attributes according to table column header
        self.relationship_instances = []

    @classmethod
    def get_user_plant_map(cls):
        query =  """SELECT * 
                    FROM plants
                    JOIN users_has_plants
                    ON users_has_plants.plants_id = plants.id
                    JOIN users
                    ON users.id = users_has_plants.users_id
                    ORDER BY
                    first_name"""
        returned_data = MySQLConnection(cls.db).query_db(query)
        print(returned_data)
        if len(returned_data) < 1:
            return False
        plants=[]
        for row in returned_data:
            plant_data = {
                "id" : row["id"],
                "name" : row["name"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"],
            }
            plant = plant_model.Plant(plant_data)
            user_data = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            user = user_model.User(user_data)
            map_data = {
                "user" : user,
                "plant" : plant,
                "water_schedule" : row["water_schedule"],
                "description" : row["description"]
            }
            
            
        return plants


