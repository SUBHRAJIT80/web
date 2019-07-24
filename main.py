#!/usr/bin/env python3

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

@app.route("/tp")
def tp():
    return render_template("template.html")

@app.route("/in")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5010,
        threaded=True,
        debug=True
    )
