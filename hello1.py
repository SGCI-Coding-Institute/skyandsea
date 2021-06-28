from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Just to make sure it works!</p>"

    
#@app.route("/go")
#def run_model():
#    return this_guy_joe.go(3000,10,0,5)


