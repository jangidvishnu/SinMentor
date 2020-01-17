from flask import Flask,render_template,request,url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail,Message
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)