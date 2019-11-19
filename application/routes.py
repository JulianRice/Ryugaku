from application import app, db
                            #db, api
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from application.models import ToukouUser
from application.forms import RegisterFormToukou, LoginFormToukou
import os
# from flask_restplus import Resource #Handles all API requests
# from application.course_list import course_list

#############################################################################
# INDEX
#############################################################################
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

#############################################################################
# LOGIN
#############################################################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginFormToukou()
    if form.validate_on_submit():
        username    = form.username.data
        password    = form.password.data

        user = ToukouUser.objects(username=username).first()
        if user and user.password == password: #Fix this later
            flash(f"{ user.lnameJp },　おかえりなさい", "success")
            session['userId']   = user.userId
            session['username'] = user.username
            session['fullname'] = user.lnameJp + user.fnameJp
            return redirect("/index")
        else:
            flash("Incorrect password or username!", "danger")
    return render_template("login.html", login=True, form=form)

#############################################################################
# REGISTER (Incomplete)
#############################################################################
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html", register=True)

#############################################################################
# USERS
#############################################################################
@app.route("/users")
def user():
    #ToukouUser(userId=0, fnameJp="万里", lnameJp="宮沢", fnameEn="Banri", lnameEn="Miyazawa", \
    #    username="banri634", email="banri634@ucla.edu", password="123312", university="UCLA", \
    #    majorType="文系", country="USA", statusNow="社会人").save()
    toukouUsers = ToukouUser.objects.all()
    return render_template("users.html", users=toukouUsers)

#############################################################################
# LOGOUT
#############################################################################
@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username', None)
    session.pop('fullname', None)
    return redirect(url_for('index'))

#############################################################################
# PROFILE
#############################################################################
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    username = session.get('username')
    user = ToukouUser.objects(username=username).first()
    if user == None:
        flash("User not found! Error!", "warning")
        return redirect(url_for('index'))
    return render_template("profile.html", profile=True, user=user)

#############################################################################
# UPLOAD (Incomplete)
#############################################################################
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    return json.dumps({'filename': f_name})