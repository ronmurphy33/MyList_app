import re
from flask_app import app 
from flask import render_template, redirect, flash, request, session 
from flask_app.models import user, list
from flask_app.models.list import List
from flask_app.models.user import User

@app.route ('/new_list')
def show_new_list():
    if 'user_id' not in session:
        return redirect ('/')
    return render_template("new_list.html")

@app.route ('/new_list', methods=['POST'])
def create_list():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "list_name" : request.form['list_name'],
        "user_id": session['user_id']
    }
    print(data)
    List.create_list(data)
    return redirect('/dashboard')

@app.route ('/delete_list/<int:id>')
def destroy_list(id):
    if 'user_id' not in session:
        return redirect ('/')
    data ={
        "id": id
    }
    List.destroy_list(data)
    return redirect('/dashboard')