from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("mongodb://eduardo:senha@200.137.131.118/cfdb")
db = client.cfdb

@app.route("/administrator/")
def index():
    return render_template("administrator.html")

from CoordenacaoFacil.controllers import UniversityController
