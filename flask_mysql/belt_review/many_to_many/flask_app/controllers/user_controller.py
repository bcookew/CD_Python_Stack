from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user_model, classes_model
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#----------------------------------
# ------------------------------------  Home Page
#----------------------------------

@app.route('/')
def home():  
    return render_template('homepage.html')

#----------------------------------
# ------------------------------------  Login Process
#----------------------------------

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email" : request.form["email"],
        "password" : request.form["password"]
    }
    user = user_model.User.validate_login(data)

    if user:
        if not bcrypt.check_password_hash(user.password, data['password']):
            flash('Invalid Email or Password!')
            return redirect('/')
    
    session['user_id'] = user.id
    
    return redirect('/dashboard')

#----------------------------------
# ------------------------------------  Register Process
#----------------------------------

@app.route('/register', methods=['POST'])
def registration():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }

    valid_form = user_model.User.validate_registration(data)
    
    if not valid_form:
        return redirect('/')
    
    data['password'] = bcrypt.generate_password_hash(request.form['password'])

    user_id = user_model.User.add_user(data)
    session["user_id"] = user_id
    return redirect('/dashboard')

#----------------------------------
# ------------------------------------  User Profile
#----------------------------------

@app.route('/dashboard')
def load_profile():
    if "user_id" in session:
        data = {
            "id": session['user_id'] 
        }
        print(data['id'])
        user = user_model.User.get_user(data)
        courses = classes_model.Course.get_courses_without_user(data)
        return render_template('dashboard.html', user=user, other_courses=courses)
    else:
        flash("Access Denied!\nYou must log in!")
        return redirect('/')


#----------------------------------
# ------------------------------------  Logout
#----------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')