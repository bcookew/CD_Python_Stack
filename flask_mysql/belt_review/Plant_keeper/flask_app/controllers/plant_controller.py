from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import plant_model

#----------------------------------
#-------------------------------------  New Plant Page load
#----------------------------------

@app.route('/newPlant')
def newPlant():
    return render_template('newPlant.html')


#----------------------------------
#-------------------------------------  Validate form and Add Plant to database
#----------------------------------

@app.route('/savePlant', methods=["POST"])
def savePlant():
    data = {
        "name" : request.form['name'],
        "water_schedule" : request.form['water_schedule'],
        "description" : request.form['description'],
        "user_id" : request.form['user_id']
    }
    plant_model.Plant.validate_form(data)
    plant_model.Plant.add_new_plant(data)
    
    return redirect('/dashboard')


