from flask_app.config.mysqlconnection import MySQLConnection

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
        returnedData = MySQLConnection('ninjas_and_dojos_schema').query_db(query)
        instances = [cls(row) for row in returnedData]
        return instances