from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/addNinja')
def addNinja():
    return render_template('addNinja.html', dojos = Dojo.getAll())

@app.route('/adding', methods=["POST"])
def adding():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.addNinja(data)
    return redirect('/dojos')