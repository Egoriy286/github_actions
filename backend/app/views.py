from app import app
from flask import render_template

servers = ["192.168.0.185", "127.0.0.1", "93df-193-37-70-254.ngrok-free.app"]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", server=servers)
