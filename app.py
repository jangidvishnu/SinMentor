from flask import Flask,render_template,request,url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail,Message
import mysql.connector

with open("config.json","r") as c:
    params=json.load(c)["params"]

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/mentors')
def show_mentors():
    return render_template('mentors.html')

@app.route('/login')
def login():
    return render_template('login.html',params=params)

@app.route('/register')
def register():
    return render_template('register.html',params=params)

@app.route('/events')
def events():
    return render_template('events.html',params=params)

app.run(debug=True)