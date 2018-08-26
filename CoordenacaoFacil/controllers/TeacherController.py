from flask import request

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Teacher import Teacher

@app.route("/app/teachers/", methods=["POST"])
def create_teacher():
    name = request.form.get("name")
    code = request.form.get("code")
    course = request.form.get("course") #Depois substituir para objeto Coordenador

    teacher = Teacher(name=name, code=code, course=course)

    teacher.createTeacher(teacher)

    return "teacher created!"


@app.route("/app/teachers/", methods=["GET"])
def get_all_teachers():
    pass

@app.route("/app/teachers/<teacher_id>/", methods=["GET"])
def get_teacher(teacher_id):
    pass


@app.route("/app/teachers/<teacher_id>/", methods=["PUT"])
def update_teacher(teacher_id):
    pass


@app.route("/app/teachers/<teacher_id>/", methods=["DELETE"])
def delete_teacher(teacher_id):
    pass
