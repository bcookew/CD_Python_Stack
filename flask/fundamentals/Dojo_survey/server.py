from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "skdflaiudbvlialvsdfvb82772fr982h89yfrh"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    print(request.form)
    for key in request.form:
        session[key] = request.form[key]
    return redirect('/submitted')

@app.route('/submitted')
def submitted():
    details = {}
    for key in session:
        details[key] = session[key]
    return render_template('submitted.html', **details)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)