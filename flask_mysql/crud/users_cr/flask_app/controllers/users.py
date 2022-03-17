from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    for user in users:
        print(user)
    return render_template("index.html", users=users)

@app.route('/addUser')
def addUser():
    return render_template("addUser.html")

@app.route('/creatingUser', methods=['POST'])
def createRecord():
    User.insert(request.form)
    return redirect('/')