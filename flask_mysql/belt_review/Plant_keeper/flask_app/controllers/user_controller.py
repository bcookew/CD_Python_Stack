from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user_model, plant_model
from flask_bcrypt import Bcrypt
from flask_mysql.belt_review.Plant_keeper.flask_app.config.validator import Logged_in
bcrypt = Bcrypt(app)

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
# ------------------------------------  Login Process
#----------------------------------

@app.route('/login', methods=['POST'])
def login():
    
    ####################  Process data from form  ####################
    data = {
        "email" : request.form["email"],
        "password" : request.form["password"]
    }

    ####################  validate form data  ####################
    user = user_model.User.validate_login(data)

    ####################  if user exists check password  ####################
    if user:
        if not bcrypt.check_password_hash(user.password, data['password']):
            flash('Invalid Email or Password!')
            return redirect('/')
    else:
        flash('Invalid Email or Password!')
        return redirect('/')
    ####################  if login, user.id in session, redir to dashboard   ####################
    session['user_id'] = user.id
    
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
        user = user_model.User.get_user(data)
        plants = plant_model.Plant.get_plants_with_owners()
        return render_template('user.html', user = user, plants = plants)
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