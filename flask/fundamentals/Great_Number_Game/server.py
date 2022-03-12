from flask import Flask, render_template, session, redirect, request, url_for
from random import randrange
app = Flask(__name__)
app.secret_key = "skdflaiudbvlialvsdfvb82772fr982h89yfrh"

@app.route('/')
def index(hiLow="",color=""):
    if "num" not in session:
        session["num"] = randrange(1,101)
        return render_template('index.html')
    elif("hiLow" in session and "color" in session):
        return render_template('index.html', hiLow=session['hiLow'], color=session['color'])
    else:
        return render_template('index.html')

        

@app.route('/guess', methods=["POST"])
def submit():
    session["guess"] = int(request.form["guess"])
    num = session["num"]
    guess = session["guess"]
    if guess == num:
        hiLow = f"You got it! It was {str(guess)}"
        color = "has-background-success"
    if guess > num:
        hiLow = f"Your guess of {str(guess)} was too high!"
        color = "has-background-danger"
    if guess < num:
        hiLow = f"Your guess of {str(guess)} was too low!"
        color = "has-background-link has-text-light"
    session["color"] = color
    session["hiLow"] = hiLow
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)