from flask_app import app, render_template

#----------------------------------
#-------------------------------------  Home Route
#----------------------------------

@app.route('/home')
def home():
    return render_template('index.html')
