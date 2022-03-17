from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninjas_model import Ninja

@app.route('/ninjas/<int:id>')
def dojoPage():
    return render_template('dojo.html')