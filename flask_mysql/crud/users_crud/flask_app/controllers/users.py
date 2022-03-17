import re
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route('/creatingUser', methods=['POST'])
def createRecord():
    User.insert(request.form)
    return redirect('/')

@app.route('/updateUser/<int:id>')
def updateUser(id):
    return render_template('updateUser.html', user=User.pullByID(id))

@app.route('/updating', methods=["POST"])
def updating():
    uID = request.form['id']
    User.updateUser(request.form)
    return redirect(f'/profile/{uID}')

@app.route('/profile/<int:num>')
def viewProfile(num):
    return render_template('profile.html', user=User.pullByID(num))

@app.route('/delete', methods=["POST"])
def deleteUser():
    User.deleteUser(request.form['id'])
    return redirect('/')

@app.route('/delete/<int:id>')
def deleteUserlink(id):
    User.deleteUser(id)
    return redirect('/')