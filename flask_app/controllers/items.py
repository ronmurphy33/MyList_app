import re
from turtle import clear
from typing import ItemsView
from flask_app import app 
from flask import render_template, redirect, flash, request, session 
from flask_app.models import user, list, item
from flask_app.models.list import List
from flask_app.models.user import User
from flask_app.models.item import Item

@app.route ('/add_items/<int:id>')
def fill_list(id):
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "id":id
    }
    active_user = {
        "user_id": session['user_id']
    }
    logged_in_user = user.User.get_user_by_id(active_user)
    print(data)
    return render_template('/add_items.html', user = logged_in_user, this_list = List.get_one_list(data), items = Item.get_all_items(data))

@app.route('/fill_list', methods = ['POST'])
def add_item():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "item_name" : request.form['item_name'],
        "category": request.form['category'],
        "list_id": request.form['id']
    }
    Item.add_item(data)
    return redirect(f"/add_items/{request.form['id']}")

@app.route('/add_items/<int:list_id>/delete_item/<int:id>')
def destroy_item(list_id,id):
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "id": id
    }
    list_id = list_id
    Item.destroy_item(data)
    return redirect(f"/add_items/{list_id}")