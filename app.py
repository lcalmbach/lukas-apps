from flask import Flask, render_template, request, redirect, url_for, g, flash
import os
from secrets import token_hex
import json
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

@app.route("/", methods=["GET"])
def home():
    f = open('apps.json')
    apps = json.load(f)
    return render_template("home.html", apps=apps)

