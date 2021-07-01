from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('first.html')

@app.route("/map")
def mapit():
    return render_template('maptest.html')

@app.route('/pictures')
def pict():
    return render_template('portrait.html')

if __name__ == '__main__':
   app.run()