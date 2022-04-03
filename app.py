from flask import Flask, render_template, request, redirect, url_for, g, flash
import os
from datetime import datetime
from secrets import token_hex
import json
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

NEW_BADGE_LIMIT = 30

@app.route("/", methods=["GET"])
def home():
    f = open('apps.json')
    apps = json.load(f)
    for app in apps:
        days_since_published = (datetime.today() - datetime.strptime(app['publish-date'],'%Y-%m-%d')).days
        app['is_new'] = True if days_since_published < NEW_BADGE_LIMIT else False
    return render_template("home.html", apps=apps)

