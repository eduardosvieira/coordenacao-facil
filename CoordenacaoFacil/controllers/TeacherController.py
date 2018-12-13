from flask import request, jsonify

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Teacher import Teacher
from CoordenacaoFacil.models.University import University
from CoordenacaoFacil.models.Course import Course

@app.route("/app/teachers/", methods=["POST"])
def create_teacher():
    name = request.form.get("name")
    email = request.form.get("email")
    code = request.form.get("code")
    password = request.form.get("password")
    createdAt = request.form.get("createdAt")
    university = University().getUniversityByCode(request.form.get("university"))
    course = Course().getCourseByCode(request.form.get("course"))

    teacher = Teacher(code=code, name=name, email=email, password=password, createdAt=createdAt, university=university, course=course)

    if teacher.create(teacher):
        return "teacher created!", 200
    else:
        return "Error", 400


@app.route("/app/teachers/", methods=["GET"])
def get_all_teachers():
    result = Teacher().getAllTeachers()

    teachers = []

    for t in result:
        teachers.append({
            "code": t["code"],
            "name": t["name"]})

    return jsonify(teachers)

@app.route("/app/teachers/<teacher_id>/", methods=["GET"])
def get_teacher(teacher_id):
    pass


@app.route("/app/teachers/<teacher_id>/", methods=["PUT"])
def update_teacher(teacher_id):
    pass


@app.route("/app/teachers/<teacher_id>/", methods=["DELETE"])
def delete_teacher(teacher_id):
    pass
