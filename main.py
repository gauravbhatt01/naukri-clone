# flask --app main run --debug

from flask import Flask
from flask import render_template
from scraper import get_jobs_data

app = Flask(__name__)

jobs_data = get_jobs_data()

@app.route("/")
def hello_world():
    return render_template("do-or-die.html")