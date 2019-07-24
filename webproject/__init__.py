import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ab")
def about():
    return render_template("about.html")

@app.route("/sal")
def salvador():
    return "Hello, Salvador!!!"

@app.route("/sal")
def salva():
    return render_template("salva.html")
@app.route("/tp")
def tp():
    return render_template("template.html")

@app.route("/in")
def index():
    return render_template("index.html")
