from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8, color1="white")

@app.route('/<int:rows>')
def numChecks(rows):
    return render_template('index.html', rows=rows, columns=8, color1="white")

@app.route('/<int:rows>/<int:columns>')
def numXY(rows, columns):
    return render_template('index.html', rows=rows, columns=columns, color1="white")

@app.route('/<int:rows>/<int:columns>/<color>/<color2>')
def numXYC(rows, columns, color, color2):
    return render_template('index.html', rows=rows, columns=columns, color1=color, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)