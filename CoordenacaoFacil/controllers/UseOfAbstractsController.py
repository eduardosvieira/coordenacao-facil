import os
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, redirect, session

from CoordenacaoFacil import app

from CoordenacaoFacil.models.UseOfAbstracts import UseOfAbstracts
from CoordenacaoFacil.models.Student import Student
from CoordenacaoFacil.models.Abstract import Abstract

UPLOAD_FOLDER = "/home/eduardo/Github/coordenacao-facil/CoordenacaoFacil/static/useOfAbstracts"

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

    path = UPLOAD_FOLDER + filename

    uoa = UseOfAbstracts(origin=origin, destiny=destiny, createdAt=createdAt, menu=path, student=Student().getUserByCode(session["code"]))

    if uoa.create(uoa):
        return "OK", 200
    else:
        return "Erro", 400
