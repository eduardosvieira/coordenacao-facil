from CoordenacaoFacil.models.User import User

from CoordenacaoFacil import db


class Coordinator(User):
    def __init__(self, id=0, code=0, name="", email="", password="", type="", createdAt="", course=None, university=None):
        super().__init__(id=id, code=code, name=name, email=email, password=password, type=type, createdAt=createdAt)
        self.course = course
        self.university = university


    def createCoordinator(self, coordinator=None):
        db.users.insert({
            "name": coordinator.name,
            "code": coordinator.code,
            "course": coordinator.course,
            "type": "coordinator"
        })

        return True

    def getAllCoordinators(self):
        coordinators = db.users.find({})

        return coordinators

    def getCoordinatorByCode(self, code):
        coordinator = db.coordinators.find_one({"code": code})

        return coordinator
