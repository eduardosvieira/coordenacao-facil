from flask import request

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Abstract import Abstract

@app.route("/app/abstracts/", methods=["POST"])
def create_abstract():
    name = request.form.get("name")
    code = request.form.get("code")
    teacher = request.form.get("teacher") #Depois substituir para objeto Course

    abstract = Abstract(name=name, code=code, teacher=teacher)

    abstract.createAbstract(abstract)

    return "abstract created!"


@app.route("/app/abstracts/", methods=["GET"])
def get_all_abstracts():
    pass

@app.route("/app/abstracts/<abstract_id>/", methods=["GET"])
def get_abstract(abstract_id):
    pass


@app.route("/app/abstracts/<abstract_id>/", methods=["PUT"])
def update_abstract(abstract_id):
    pass


@app.route("/app/abstracts/<abstract_id>/", methods=["DELETE"])
def delete_abstract(abstract_id):
    pass
