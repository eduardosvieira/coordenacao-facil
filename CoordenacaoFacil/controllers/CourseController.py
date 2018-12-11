from flask import request, jsonify

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Course import Course
from CoordenacaoFacil.models.Coordinator import Coordinator
from CoordenacaoFacil.models.University import University

@app.route("/app/courses/", methods=["POST"])
def create_course():
    name = request.form.get("name")
    code = request.form.get("code")
    print(request.form.get("university"))
    university = University().getUniversityByCode(request.form.get("university"))
    coordinator = Coordinator().getCoordinatorByCode(request.form.get("coordinator"))
    createdAt = request.form.get("createdAt")

    course = Course(name=name, code=code, coordinator=coordinator, university=university, createdAt=createdAt)

    course.createCourse(course)

    return "Course created!"


@app.route("/app/courses/", methods=["GET"])
def get_all_courses():
    course = Course()

    result = course.getAllCourses()

    courses = []

    for i in result:
        courses.append({"name": i["name"], "code": i["code"]})

    return jsonify(courses)

@app.route("/app/courses/<course_id>/", methods=["GET"])
def get_course(course_id):
    pass


@app.route("/app/courses/<course_id>/", methods=["PUT"])
def update_course(course_id):
    pass


@app.route("/app/courses/<course_id>/", methods=["DELETE"])
def delete_course(course_id):
    pass
