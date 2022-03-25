from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<int:id>')
def get_one_user(id):
    data = {"id":id}
    user = User.get_one_by_id(data)
    print(user)
    print(jsonify(user))
    return jsonify(user)

@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
    user = User.save(request.form)
    
    return jsonify(user)



