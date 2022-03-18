# import flask app framework
from flask_app import app

# import controllers for routing
from flask_app.controllers import dojos_controller
from flask_app.controllers import ninjas_controller


# launch server if this script run directly
if __name__=="__main__":
    app.run(debug=True)