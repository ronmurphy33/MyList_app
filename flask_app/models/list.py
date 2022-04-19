from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import user
import re 

class List:
    schema ="mylist"

    def __init__(self, data):
        self.id = data['id']
        self.list_name = data['list_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod
    def create_list(cls, data):
        query = "INSERT into lists (list_name, user_id) VALUES (%(list_name)s, %(user_id)s)"
        results = MySQLConnection(cls.schema).query_db(query, data)