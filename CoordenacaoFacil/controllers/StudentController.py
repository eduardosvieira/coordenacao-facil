from flask import session, request, render_template, redirect

from CoordenacaoFacil import app

from CoordenacaoFacil.models.University import University
from CoordenacaoFacil.models.Course import Course
from CoordenacaoFacil.models.Student import Student

@app.route("/app/login/", methods=["POST"])
def check_login():
    name = request.form.get("name")
    email = request.form.get("email")
    code = request.form.get("code")
    password = request.form.get("password")
    createdAt = request.form.get("createdAt")
    university = University().getUniversityByCode(request.form.get("university"))
    course = Course().getCourseByCode(request.form.get("course"))

    user = Student(code=code, name=name, email=email, password=password, createdAt=createdAt, university=university, course=course)

    if user.create(user):
        return redirect("/app/login/")
    else:
        return render_template("signup/signup.html", error="Houve um problema ao tentar cadastrar estudante. Tente novamente.")
