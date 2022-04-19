import re
from turtle import clear
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
    return render_template('/add_items.html', user = logged_in_user, this_list = list.List.get_one_list(data))