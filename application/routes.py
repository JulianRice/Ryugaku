from application import app, db
                            #db, api
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from application.models import ToukouUser
from application.forms import RegisterFormToukou, LoginFormToukou
# from flask_restplus import Resource #Handles all API requests
# from application.course_list import course_list

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginFormToukou()
    if form.validate_on_submit():
        username    = form.username.data
        password    = form.password.data

        user = ToukouUser.objects(username=username).first()
        if user and user.password == password:
            flash(f"{ user.lnameJp },　おかえりなさい", "success")
            session['userId']   = user.userId
            session['username'] = user.username
            session['fullname'] = user.lnameJp + user.fnameJp
            return redirect("/index")
        else:
            flash("Incorrect password or username!", "danger")
    return render_template("login.html", login=True, form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html", register=True)

@app.route("/users")
def user():
    #ToukouUser(userId=0, fnameJp="万里", lnameJp="宮沢", fnameEn="Banri", lnameEn="Miyazawa", \
    #    username="banri634", email="banri634@ucla.edu", password="123312", university="UCLA", \
    #    majorType="文系", country="USA", statusNow="社会人").save()
    toukouUsers = ToukouUser.objects.all()
    return render_template("users.html", users=toukouUsers)

@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username', None)
    session.pop('fullname', None)
    return redirect(url_for('index'))

@app.route("/profile")
def profile():
    return redirect(url_for('index'))