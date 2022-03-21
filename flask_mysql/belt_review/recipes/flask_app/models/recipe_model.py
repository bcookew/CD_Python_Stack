from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.config.validator import Text_Field

class Recipe:
    db = "recipes_schema" # Schema name here

    def __init__(self, data): # layout instance attributes according to table column header
        self.id = data['id']
        self.user_id = data["users_id"]
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_on = data['made_on']
        self.less_than_30 = data['less_than_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


############# Class Methods for interacting with the database #############

#---------------------------------
# ----------------------------------- Get All Recipes by user_id
# --------------------------------

    @classmethod 
    def get_all_recipes_by_user_id(cls, data):
        query =  "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        recipe_instances = [cls(row) for row in returnedData]
        return recipe_instances

#---------------------------------
# ----------------------------------- Get Recipe by ID
# --------------------------------

    @classmethod 
    def get_recipe_by_id(cls, data):
        query =  "SELECT * FROM recipes WHERE id = %(id)s;"
        returnedData = MySQLConnection(cls.db).query_db(query, data)
        recipe_instance = cls(returnedData[0])
        return recipe_instance

#---------------------------------
# ----------------------------------- Add Recipe
# --------------------------------

    @classmethod 
    def add_recipe(cls, data):
        query =  """INSERT INTO recipes (
                        name, users_id, description, instructions, made_on, less_than_30, created_at
                    )
                    VALUES(
                        %(name)s, %(users_id)s, %(description)s, %(instructions)s, %(made_on)s, %(less_than_30)s, NOW());
                    """
        returned = MySQLConnection(cls.db).query_db(query, data)
        return returned


#---------------------------------
# ----------------------------------- Update Recipe
# --------------------------------

    @classmethod 
    def update_recipe(cls, data):
        query =  """UPDATE recipes
                    SET
                    name = %(name)s, 
                    description = %(description)s, 
                    instructions = %(instructions)s, 
                    less_than_30 = %(less_than_30)s, 
                    updated_at = NOW()
                    WHERE
                    id = %(id)s;
                    """
        returned = MySQLConnection(cls.db).query_db(query, data)
        return returned


#---------------------------------
# ----------------------------------- Delete Recipe
# --------------------------------

    @classmethod 
    def delete_recipe(cls, data):
        query =  "DELETE FROM recipes WHERE id = %(id)s;"
        MySQLConnection(cls.db).query_db(query, data)
        return

#####################################################
############# Static Methods as helpers #############
#####################################################

#---------------------------------
# ----------------------------------- Form Validation
# --------------------------------

    @staticmethod
    def validate_recipe(data):
        valid_form = True
        print("\n", data['name'], "\n")
        if not Text_Field(4).inspect(data['name']):
            flash('Recipe name must be between 4-255 characters!')
            valid_form = False

        print("\n", data['description'], "\n")
        if not Text_Field(10).inspect(data['description']):
            flash('Description must be between 10-255 characters!')
            valid_form = False

        print("\n", data['instructions'], "\n")
        if not Text_Field(20, 1000).inspect(data['instructions']):
            flash("First name must be at least 20 characters!")
            valid_form = False

        print("\n", data['made_on'], "\n")
        if not data['made_on']:
            flash("Select when you first made the recipe!")
            valid_form = False

        return valid_form