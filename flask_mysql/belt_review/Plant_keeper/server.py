from flask_app import app
from flask_app.controllers import user_controller, index_controller, plant_controller

if __name__ == "__main__":
    app.run(debug=True)