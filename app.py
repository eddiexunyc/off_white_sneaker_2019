import os
from flask import Flask, render_template, redirect, url_for, jsonify


# Create an instance of Flask
app = Flask(__name__, static_url_path = "")

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)