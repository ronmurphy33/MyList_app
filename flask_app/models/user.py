from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import list
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class  User:
    schema ="mylist"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.lists = []

    @staticmethod
    def validate_reg(form):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = MySQLConnection('mylist').query_db(query, form)

        if len(results) >= 1:
            flash ("Email address is already registered", "register")
            is_valid = False
        if len(form['first_name']) < 2:
            flash ("First name field must be at least 2 characters","register")
            is_valid = False
        if len(form['last_name']) < 2:
            flash ("Last name field must be at least 2 characters","register")
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash ("A valid email address is required","register")
            is_valid = False
        if len(form['password']) < 6:
            flash ("Password must be at least 6 characters","register")
            is_valid = False
        if form['password'] != form['confirm_password']:
            flash('passwords must be an exact match',"register")
            is_valid = False
        return is_valid
