import re
from turtle import clear
from flask_app import app 
from flask import render_template, redirect, flash, request, session 
from flask_app.models import user, list
from flask_app.models.user import User

@app.route ('/new_list')
def show_new_list():
    if 'user_id' not in session:
        return redirect ('/')
    return render_template("new_list.html")

@app.route('/create_list', methods=['POST']
def create_list():
    pass