from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUE (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s)"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results