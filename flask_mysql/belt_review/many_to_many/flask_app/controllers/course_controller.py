from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user_model, classes_model
from flask_app.config.validator import Logged_in

##############################
################################# Enroll student in class
##############################

@app.route('/enroll/<int:id>')
def enroll(id):
    print("\n\nIN ENROLL\n\n")
    Logged_in.log_in_checker()
    
    data = {
        "students_id" : session['user_id'],
        "classes_id" : id
    }

    user_model.User.enroll(data)

    return redirect('/dashboard')

##############################
################################# Remove student from class
##############################

@app.route('/un_enroll/<int:id>')
def un_enroll(id):
    Logged_in.log_in_checker()
    data = {
        "students_id" : session['user_id'],
        "classes_id" : id
    }

    user_model.User.un_enroll(data)

    return redirect('/dashboard')

##############################
################################# View course listing
##############################

@app.route('/view_course/<int:id>')
def view_course(id):
    Logged_in.log_in_checker()
    data = {
        "classes_id" : id
    }
    return render_template('view_class.html', course = classes_model.Course.get_course_with_students(data))

