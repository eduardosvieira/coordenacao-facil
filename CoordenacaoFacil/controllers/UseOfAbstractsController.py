import os
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, redirect, session, render_template, jsonify, send_from_directory

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
    try:
        uoa = UseOfAbstracts().getUOAByCode(request.form.get("uoa-code"))
        teacher = Teacher().getTeacherByCode(request.form.get("teacher"))

        msg = Message(
          "Coordenação Fácil - Pedido de Aproveitamento de Cadeiras",
          sender='lawsclassroom@gmail.com',
          recipients=[teacher["email"]])
        with app.open_resource(app.static_folder + uoa["menu"]) as fp:
            msg.attach("Ementa.pdf", "application/pdf", fp.read())

            first = "INFORMAÇÕES GERAIS<br>" + "TURMA CURSADA: {0} ({1})<br>".format(uoa["origin"]["name"], uoa["origin"]["code"]) + "TURMA PRETENDIDA: {0} ({1})<br>".format(uoa["destiny"]["name"], uoa["destiny"]["code"])
            second = "<br>INFORMAÇÕES DE LOGIN<br>" + "CÓDIGO: {0}<br>".format(teacher["code"]) + "SENHA: {}<br>".format(teacher["password"])
            msg.html = first + second
            mail.send(msg)

        return redirect("/app/coordinator/")
    except:
        print("E-mail não enviado.")
        return "Houve um problema ao encaminhar e-mail.", 400


@app.route("/app/useOfAbstracts/", methods=["POST"])
def create_uoa():
    origin = Abstract().getAbstractByCode(request.form.get("uoa-origin"))
    destiny = Abstract().getAbstractByCode(request.form.get("uoa-destiny"))
    createdAt = request.form.get("uoa-createdAt")

    #recuperando ementa do curso
    menu = request.files["uoa-menu"]
    #generando um token para identificar a ementa na pasta
    filename = generate_password_hash(menu.filename) + ".pdf"
    #salvando a ementa no dataset
    menu.save(os.path.join(UPLOAD_FOLDER, filename))

    path = "/useOfAbstracts/" + filename

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


@app.route("/app/useOfAbstracts/<id>/", methods=["GET"])
def get_uoa(id):
    uoa = UseOfAbstracts().getByCode(id)

    if uoa:
        uoa["_id"] = str(uoa["_id"])
        uoa["origin"] = {"code": uoa["origin"]["code"], "name": uoa["origin"]["name"]}
        uoa["destiny"] = {"code": uoa["destiny"]["code"], "name": uoa["destiny"]["name"]}
        uoa["student"] = {}

        return jsonify(uoa)
    else:
        return "Houve um problema ao deletar um Aproveitamento de Cadeiras.", 400


@app.route("/app/download/<path:path>/", methods=["GET"])
def download(path):
    return send_from_directory(app.static_folder + "/", path)
    #return app.static_folder + "/" + path
