from application import app
                            #db, api
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
# from application.models import User, Course, Enrollment
# from application.forms import LoginForm, RegisterForm
# from flask_restplus import Resource #Handles all API requests
# from application.course_list import course_list

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)