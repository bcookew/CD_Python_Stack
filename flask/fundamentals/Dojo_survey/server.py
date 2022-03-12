from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "skdflaiudbvlialvsdfvb82772fr982h89yfrh"

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 1
    else: 
        session["counter"] += 1

    return render_template('index.html', counter=session["counter"])

@app.route('/2')
def plus2():
    session["counter"] += 2

    return render_template('index.html', counter=session["counter"])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)