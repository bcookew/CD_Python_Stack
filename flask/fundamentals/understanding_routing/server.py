from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return word*num

@app.errorhandler(404)
def missing(error):
    return 'Sorry! No response. Try Again.'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.