from sqlite3 import connect
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos(name) VALUE (%(name)s);"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja))
        return dojo