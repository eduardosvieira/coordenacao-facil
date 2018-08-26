from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("mongodb://eduardo:senha@200.137.131.118/cfdb")
db = client.cfdb

from CoordenacaoFacil.controllers import UniversityController
from CoordenacaoFacil.controllers import CourseController
from CoordenacaoFacil.controllers import CoordinatorController

from CoordenacaoFacil.models.University import University
from CoordenacaoFacil.models.Course import Course
from CoordenacaoFacil.models.Coordinator import Coordinator

@app.route("/administrator/")
def admin():
    universities = University().getAllUniversities()
    courses = Course().getAllCourses()
    coordinators = Coordinator().getAllCoordinators()

    return render_template("administrator.html", universities=universities, courses=courses, coordinators=coordinators)
