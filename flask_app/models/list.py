from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import user
import re 
from asyncio import all_tasks


class List:
    schema ="mylist"

    def __init__(self, data):
        self.id = data['id']
        self.list_name = data['list_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def create_list(cls, data):
        query = "INSERT into lists (list_name, user_id, created_at, updated_at) VALUES (%(list_name)s, %(user_id)s, NOW, NOW)"
        results = MySQLConnection(cls.schema).query_db(query, data)
    
    # @classmethod
    # def get_all_lists_with_user(cls):
    #     query = "SELECT * from lists LEFT JOIN users on lists.user_id = users.id"
    #     results = connectToMySQL(cls.schema).query_db(query)
    #     lists_all = []
    #     for this_list in results:
    #         list_instance = cls(this_list)
    #         user_data = {
    #             "id" : this_list['id'],
    #             "first_name" : this_list['first_name'],
    #             "last_name" : this_list['last_name'],
    #             "email" : this_list['email'],
    #             "password" : this_list['password'],
    #             "created_at" : this_list['created_at'],
    #             "updated_at" : this_list['updated_at']
    #         }
    #         this_user = user.User(user_data)
    #         list_instance.user = this_user 
    #         lists_all.append(list_instance)
    #     return lists_all
    #     for r in results:
    #         lists_all.append(cls(r))
    #     print(lists_all)
    #     return lists_all
    
    @classmethod
    def lists_get_all(cls):
        query = "SELECT * FROM lists"
        results = connectToMySQL('mylist').query_db(query)
        lists_all = []
        for list in results:
            lists_all.append(cls(list))
        print(lists_all)
        return lists_all


    @classmethod
    def get_one_list(cls, data):
        query = "SELECT * FROM lists WHERE lists.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def destroy_list(cls, data):
        query = ("DELETE FROM lists WHERE id = %(id)s;")
        results = connectToMySQL(cls.schema).query_db(query, data)

