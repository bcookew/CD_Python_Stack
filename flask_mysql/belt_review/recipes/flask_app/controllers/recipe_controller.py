from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import recipe_model

#----------------------------------
# ------------------------------------  Save Recipe
#----------------------------------

@app.route('/saveRecipe', methods=['POST'])
def save_recipe():
    data = {
        "users_id" : request.form["user_id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "made_on" : request.form["made_on"],
        "less_than_30" : request.form["less_than_30"]
    }

    valid_form = recipe_model.Recipe.validate_recipe(data)
    
    if not valid_form:
        return redirect('/create')

    recipe_model.Recipe.add_recipe(data)
    return redirect('/dashboard')


#----------------------------------
# ------------------------------------  Create Recipe
#----------------------------------

@app.route('/create')
def recipe_form():
    return render_template('add_recipe.html')


#----------------------------------
# ------------------------------------  View Recipe
#----------------------------------

@app.route('/viewRecipe/<int:id>')
def view_recipe(id):
    data = {
        "id" : id
    }
    return render_template('view_recipe.html', recipe = recipe_model.Recipe.get_recipe_by_id(data))


#----------------------------------
# ------------------------------------  Edit Recipe
#----------------------------------

@app.route('/editRecipe/<int:id>')
def edit_recipe(id):
    data = {
        "id" : id
    }
    return render_template('edit_recipe.html', recipe = recipe_model.Recipe.get_recipe_by_id(data))

#----------------------------------
# ------------------------------------  Process Edit Recipe
#----------------------------------


@app.route('/saveEdit', methods=["POST"])

def save_edit():
    data = {
        "id" : request.form["id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "made_on" : request.form["made_on"],
        "less_than_30" : request.form["less_than_30"]
    }
    recipe_model.Recipe.update_recipe(data)
    return redirect('/dashboard')

#----------------------------------
# ------------------------------------  Delete Recipe
#----------------------------------

@app.route('/deleteRecipe/<int:id>')
def delete_recipe(id):
    data = {
        "id" : id
    }
    recipe_model.Recipe.delete_recipe(data)
    return redirect('/dashboard')

