from flask import app, render_template
from flask_app import app

#----------------------------------
#-------------------------------------  Home Route
#----------------------------------

@app.route('/home')
def home():
    return render_template('index.html')
