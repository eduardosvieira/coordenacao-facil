from flask import request, jsonify

from CoordenacaoFacil import app

from CoordenacaoFacil.models.Coordinator import Coordinator
from CoordenacaoFacil.models.University import University
from CoordenacaoFacil.models.Course import Course

@app.route("/app/coordinators/", methods=["POST"])
def create_coordinator():
    name = request.form.get("name")
    email = request.form.get("email")
    code = request.form.get("code")
    password = request.form.get("password")
    createdAt = request.form.get("createdAt")
    university = University().getUniversityByCode(request.form.get("university"))
    course = Course().getCourseByCode(request.form.get("course"))

    print(email)

    coordinator = Coordinator(code=code, name=name, email=email, password=password, createdAt=createdAt, university=university, course=course)

    if coordinator.createCoordinator(coordinator):
        return "coordinator created!", 200
    else:
        return "Error", 400


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
