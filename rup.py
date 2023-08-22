from flask import Flask, render_template

app = Flask(__name__)


@app.route("/other.css") 
def indexs():
    return render_template("other.css")

@app.route("/") 
def index():
    return render_template("RUP.html")

app.run(host="0.0.0.0", port=80)
