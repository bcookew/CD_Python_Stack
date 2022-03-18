from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import survey
app.secret_key = "lafgahgoliehvbajkncv"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    print("\nForm details:")
    for key,value in request.form.items():
        print(f"{key} : {value}")
    data = {
        "name" : request.form['name'],
        "email" : request.form['email'],
        "location" : request.form['campus'],
        "language" : request.form['favLang'],
        "comment" : request.form['comment']
    }
    if not survey.Survey.validate_fields(data):
        return redirect('/')
    survey.Survey.submitSurvey(data)
    return redirect('/')

@app.route('/submitted')
def submitted():
    details = {}
    for key in session:
        details[key] = session[key]
    return render_template('submitted.html', **details)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')