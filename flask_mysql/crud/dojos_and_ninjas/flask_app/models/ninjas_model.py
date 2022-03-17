from flask_app.config.mysqlconnection import MySQLConnection

class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls) -> list:
        query = "SELECT * FROM ninjas ORDER BY name;"
        returnedData = MySQLConnection('ninjas_and_dojos_schema').query_db(query)
        instances = [cls(row) for row in returnedData]
        return instances