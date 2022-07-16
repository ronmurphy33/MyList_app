from flask import Flask, session
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = "spongebob_squarepants"

