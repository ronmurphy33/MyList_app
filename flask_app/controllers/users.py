import re
from flask_app import app 
from flask import render_template, redirect, flash, request, session 
from flask_app.models import user, list
from flask_app.models.user import User
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
    return redirect('/register')
