from flask import request, jsonify

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Coordinator import Coordinator

@app.route("/app/coordinators/", methods=["POST"])
def create_coordinator():
    name = request.form.get("name")
    code = request.form.get("code")
    course = request.form.get("course") #Depois substituir para objeto Course

    coordinator = Coordinator(name=name, code=code, course=course)

    coordinator.createCoordinator(coordinator)

    return "coordinator created!"


@app.route("/app/coordinators/", methods=["GET"])
def get_all_coordinators():
    result = Coordinator().getAllCoordinators()

    coordinators = []

    for i in Coordinator().getAllCoordinators():
        #i["_id"] = str(i["_id"])
        #coordinators.append(i)
        print(i)
    #print(coordinators)
    return jsonify(coordinators)

@app.route("/app/coordinators/<coordinator_id>/", methods=["GET"])
def get_coordinator(coordinator_id):
    pass


@app.route("/app/coordinators/<coordinator_id>/", methods=["PUT"])
def update_coordinator(coordinator_id):
    pass


@app.route("/app/coordinators/<coordinator_id>/", methods=["DELETE"])
def delete_coordinator(coordinator_id):
    pass
