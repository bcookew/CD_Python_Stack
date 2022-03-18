from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojos_model import Dojo

@app.route('/dojos')
def homePage():    
    return render_template('index.html', dojos = Dojo.getAll())

@app.route('/addDojo', methods=["POST"])
def addDojo():
    data = {
        "name" : request.form['dojo_name']
    }
    Dojo.addDojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojoPage(id):
    data = {
            "id":id
        }
    return render_template('dojo.html', dojo = Dojo.getDojoWithNinjas(data))