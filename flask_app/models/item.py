from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import list
import re 

class Item:
    schema ="mylist"

    def __init__(self, data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.list_id = data['list_id']

    @classmethod
    def add_item(cls, data):
        query = "INSERT into items (item_name, category, list_id) VALUES (%(item_name)s, %(category)s, %(list_id)s)"
        results = MySQLConnection(cls.schema).query_db(query, data)
    
    # @classmethod
    # def get_all_items_on_list(cls, data):
    #     query = "SELECT * FROM items LEFT JOIN lists on items.list_id = %(id)s"
    #     results = connectToMySQL(cls.schema).query_db(query)
    #     items_all = []
    #     for this_item in results:
    #         item_instance = cls(this_item)
    #         list_data = {
    #             "id" : this_item['id'],
    #             "list_name" : this_item['list_name'],
    #             "created_at" : this_item['created_at'],
    #             "updated_at" : this_item['updated_at']
    #         }
    #         this_list =list.List(list_data)
    #         item_instance.list = this_list
    #         items_all.append(item_instance)
    #     return items_all
    #     for r in results:
    #         items_all.append((cls(r)))
    #     print(items_all)
    #     return items_all

    @classmethod
    def get_all_items(cls, data):
        query = "SELECT * FROM items WHERE list_id = %(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        items_all = []
        for item in results:
            items_all.append(cls(item))
        print(items_all)
        return items_all

    @classmethod
    def destroy_item(cls, data):
        query = (" DELETE FROM items WHERE id = %(id)s;")
        results = connectToMySQL(cls.schema).query_db(query, data)