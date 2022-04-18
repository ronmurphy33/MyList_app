from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import user
import re 

class List:
    schema ="mylist"

    def __init__(self, data):
        pass