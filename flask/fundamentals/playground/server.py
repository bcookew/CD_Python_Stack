from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/play")
def boxes():
    return render_template('play.html', times=9)

@app.route("/play/<int:num>")
def boxUserCount(num):
    return render_template('play.html', times=num, color="rebeccapurple")

@app.route("/play/<int:num>/<color>")
def boxUserCountColor(num, color):
    return render_template('play.html', times=num, color=color)

if __name__=="__main__":
    app.run(debug=True)