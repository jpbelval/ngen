from flask import Flask, render_template, request
import ngenerator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/gen", methods=["POST"])
def gennames():
    race = request.form.get("nametype")
    namelist = ngenerator.main(race)
    return render_template('home.html', gen=True, namelist=namelist)

@app.route("/info")
def info():
    return render_template('info.html')
