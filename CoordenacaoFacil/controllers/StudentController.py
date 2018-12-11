from flask import session, request, render_template, redirect

from CoordenacaoFacil import app

@app.route("/app/login/", methods=["POST"])
def check_login():
    name = request.form.get("name")
    email = request.form.get("email")
    code = request.form.get("code")
    password = request.form.get("password")
    createdAt = request.form.get("createdAt")

    user = Student(code=code, name=name, email=email, password=password, createdAt=createdAt)

    if user.create(user):
        return redirect("/app/login/")
    else:
        return render_template("signup/signup.html", error="Houve um problema ao tentar cadastrar estudante. Tente novamente.")
