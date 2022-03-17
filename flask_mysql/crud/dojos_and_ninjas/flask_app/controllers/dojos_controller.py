from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojos_model import Dojo

@app.route('/')
def homePage():
    return render_template('index.html')