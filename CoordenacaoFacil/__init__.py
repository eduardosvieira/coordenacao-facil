from flask import Flask, render_template, session
from pymongo import MongoClient


app = Flask(__name__)

app.config["SECRET_KEY"] = "@eduardo"

client = MongoClient("mongodb://127.0.0.1/cfdb")

db = client.cfdb

from CoordenacaoFacil.controllers import UniversityController
from CoordenacaoFacil.controllers import CourseController
from CoordenacaoFacil.controllers import CoordinatorController
from CoordenacaoFacil.controllers import TeacherController
from CoordenacaoFacil.controllers import AbstractController
from CoordenacaoFacil.controllers import StudentController

from CoordenacaoFacil.models.University import University
from CoordenacaoFacil.models.Course import Course
from CoordenacaoFacil.models.Coordinator import Coordinator
from CoordenacaoFacil.models.Teacher import Teacher
from CoordenacaoFacil.models.Abstract import Abstract
from CoordenacaoFacil.models.Student import Student

@app.route("/app/")
def index():
    if "code" in session:
        user = Student().getUserByCode(session["code"])

        if user["type"] == "student":
            return render_template("student.html", user=user)
        elif user["type"] == "coordinator":
            return render_template("coordinator.html", user=user)
        elif user["type"] == "teacher":
            return render_template("teacher.html", user=user)
        else:
            return render_template("administrator.html", user=user)


@app.route("/app/login/")
def login():
    return render_template("login/login.html")


@app.route("/app/signup/")
def signup():
    return render_template("signup/signup.html")

@app.route("/teacher/")
def teacher():
    return render_template("teacher.html")

@app.route("/administrator/")
def admin():
    universities = University().getAllUniversities()
    courses = Course().getAllCourses()
    coordinators = Coordinator().getAllCoordinators()

    return render_template("administrator.html", universities=universities, courses=courses, coordinators=coordinators)

@app.route("/student/")
def student():
    return render_template("student.html")

@app.route("/coordinator/")
def coordinator():
    teachers = Teacher().getAllTeachers()
    abstracts = Abstract().getAllAbstracts()

    return render_template("coordinator.html", teachers=teachers, abstracts=abstracts)
