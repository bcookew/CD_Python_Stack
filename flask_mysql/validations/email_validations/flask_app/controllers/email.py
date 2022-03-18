from flask_app import app
from flask import redirect, request, render_template
from flask_app.models import email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
            "email" : request.form['email'],
        }
    if not email.Email.validate(data):
        return redirect('/')

    email.Email.addEmail(data)

    return redirect('/submissions')

@app.route('/submissions')
def submissions():
    return render_template('submissions.html', emails = email.Email.getAll())