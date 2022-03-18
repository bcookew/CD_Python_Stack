from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def getAll(cls) -> list:
        query = "SELECT * FROM dojos ORDER BY name;"
        returnedData = MySQLConnection('dojos_and_ninjas_schema').query_db(query)
        instances = [cls(row) for row in returnedData]
        return instances
    
    @classmethod
    def addDojo(cls,data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW())"
        returnedData = MySQLConnection('dojos_and_ninjas_schema').query_db(query, data)
        print(f"Returned Data: {returnedData}\n")

    @classmethod
    def getDojoWithNinjas(cls,data):
        
        query =  """SELECT * 
                    FROM dojos
                    JOIN ninjas
                    ON dojos.id = ninjas.dojo_id
                    WHERE dojos.id = %(id)s
                    """
        returnedData = MySQLConnection('dojos_and_ninjas_schema').query_db(query, data)
        # r = 1
        # for row in returnedData:
        #     print(f"\nRow {r}:")
        #     for key, value in row.items():
        #         print(key," : ", value)
        #     print("\n")
        #     r += 1 
        dojo_instance = cls(returnedData[0])
        for row in returnedData:
            ninja_instance = Ninja({
                    "id" : row["ninjas.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "age" : row["age"],
                    "dojo_id" : row["dojo_id"],
                    "created_at" : row["ninjas.created_at"],
                    "updated_at" : row["ninjas.updated_at"]
                })
            dojo_instance.ninjas.append(ninja_instance)
        print(dojo_instance)

        return dojo_instance