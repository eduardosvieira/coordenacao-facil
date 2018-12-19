import os
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, redirect, session, render_template
from flask_mail import Message
from CoordenacaoFacil import app

from CoordenacaoFacil.models.UseOfAbstracts import UseOfAbstracts
from CoordenacaoFacil.models.Student import Student
from CoordenacaoFacil.models.Abstract import Abstract
from CoordenacaoFacil.models.Teacher import Teacher

UPLOAD_FOLDER = "/home/eduardo/Github/coordenacao-facil/CoordenacaoFacil/static/useOfAbstracts"

from CoordenacaoFacil import mail

@app.route("/app/send/uoa/to/teacher/", methods=["POST"])
def sendUOAToTeacher():
    uoa = UseOfAbstracts().getUOAByCode(request.form.get("uoa-code"))
    teacher = Teacher().getTeacherByCode(request.form.get("teacher"))

    msg = Message(
      "Titulo",
      sender='lawsclassroom@gmail.com',
      recipients=["edusvieirap@gmail.com"])
    with app.open_resource(uoa["menu"]) as fp:
        msg.attach("ementa.pdf", "application/pdf", fp.read())

        msg.html = "Oi"
        mail.send(msg)

    return "OK"


@app.route("/app/useOfAbstracts/", methods=["POST"])
def create_uoa():
    origin = Abstract().getAbstractByCode(request.form.get("uoa-origin"))
    destiny = Abstract().getAbstractByCode(request.form.get("uoa-destiny"))
    createdAt = request.form.get("uoa-createdAt")

    #recuperando ementa do curso
    menu = request.files["uoa-menu"]
    #generando um token para identificar a ementa na pasta
    filename = generate_password_hash(menu.filename)
    #salvando a ementa no dataset
    menu.save(os.path.join(UPLOAD_FOLDER, filename))

    path = UPLOAD_FOLDER +"/"+ filename

    uoa = UseOfAbstracts(origin=origin, destiny=destiny, createdAt=createdAt, menu=path, student=Student().getUserByCode(session["code"]))

    if uoa.create(uoa):
        return redirect("/app/")
    else:
        return "Houve um problema ao criar um novo Aproveitamento de Cadeiras.", 400

@app.route("/app/useOfAbstracts/<id>/", methods=["DELETE"])
def delete_uoa(id):
    uoa = UseOfAbstracts()

    if uoa.delete(id):
        return "OK", 200
    else:
        return "Houve um problema ao deletar um Aproveitamento de Cadeiras.", 400
