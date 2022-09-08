import re
from turtle import clear
from flask_app import app 
from flask import render_template, redirect, flash, request, session 
from flask_app.models import user, list
from flask_app.models.user import User
from flask_app.models.list import List 
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def show_registration_form():
    return render_template('register.html')

@app.route('/validate_reg', methods=['POST'])
def validate_registration():
    if not User.validate_reg(request.form):
        return redirect('/register')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.register_user(data)
    return redirect('/dashboard')

@app.route ('/dashboard')
def show_dashboard():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "user_id": session['user_id']
    }
    logged_in_user = user.User.get_user_by_id(data)
    return render_template("dashboard.html", user = logged_in_user, lists = List.lists_get_all())

@app.route ('/validate_login', methods =['POST'])
def validate_login ():
    user = User.validate_email(request.form)
    if not user:
        flash ('invalid login credentials', 'login')
        return redirect ('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ('invalid login credentials', 'login')
        return redirect ('/')
    session['user_id'] = user.id
    return redirect ('/dashboard')

@app.route ('/logout')
def user_logout():
    session.clear()
    return redirect ('/')
