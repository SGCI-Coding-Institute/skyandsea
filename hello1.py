from flask import Flask, render_template
app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/map")
def mapit():
    return render_template('Introduction.html')

@app.route('/pictures')
def pict():
    return render_template('portrait.html')

if __name__ == '__main__':
   app.run()