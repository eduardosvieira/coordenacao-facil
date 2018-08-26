from flask import request

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Course import Course

@app.route("/app/courses/", methods=["POST"])
def create_course():
    name = request.form.get("name")
    code = request.form.get("code")
    coordinator = request.form.get("coordinator") #Depois substituir para objeto Coordenador

    course = Course(name=name, code=code, coordinator=coordinator)

    course.createCourse(course)

    return "Course created!"


@app.route("/app/courses/", methods=["GET"])
def get_all_courses():
    pass

@app.route("/app/courses/<course_id>/", methods=["GET"])
def get_course(course_id):
    pass


@app.route("/app/courses/<course_id>/", methods=["PUT"])
def update_course(course_id):
    pass


@app.route("/app/courses/<course_id>/", methods=["DELETE"])
def delete_course(course_id):
    pass
