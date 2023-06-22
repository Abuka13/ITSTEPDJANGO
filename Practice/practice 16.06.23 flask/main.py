import requests
import json
from flask import Flask, request, render_template, redirect, url_for

import random
app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder = 'static')
@app.route("/")
def home_page():
    data = requests.get(url="https://jsonplaceholder.typicode.com/posts").json()

    return render_template("home.html", data = data)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug = True)