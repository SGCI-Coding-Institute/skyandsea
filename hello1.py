from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "okay!"

    
#@app.route("/go")
#def run_model():
#    return this_guy_joe.go(3000,10,0,5)


