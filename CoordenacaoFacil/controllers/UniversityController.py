from flask import request

from CoordenacaoFacil import app
from CoordenacaoFacil.models.University import University


@app.route("/app/universities/", methods=["GET"])
def get_all_universities():
    pass


@app.route("/app/universities/<university_id>/", methods=["GET"])
def get_university(university_id):
    pass


@app.route("/app/universities/", methods=["POST"])
def create_university():
    name = request.form.get("name")
    code = request.form.get("code")

    university = University(code=code, name=name)

    university.createUniversity(university)

    return "University created!"


@app.route("/app/universities/<university_id>/", methods=["PUT"])
def update_university(university_id):
    pass


@app.route("/app/universities/<university_id>/", methods=["DELETE"])
def delete_university(university_id):
    pass
