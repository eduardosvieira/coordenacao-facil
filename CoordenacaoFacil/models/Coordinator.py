from werkzeug.security import generate_password_hash, check_password_hash

from CoordenacaoFacil import db

class Coordinator():
    def __init__(self, code=0, name="", email="", password="", createdAt="", course=None, university=None):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.university = university
        self.course = course
        self.createdAt = createdAt
        self.type = "coordinator"

    def createCoordinator(self, coordinator=None):
        db.coordinators.insert({
            "code": coordinator.code,
            "name": coordinator.name,
            "email": coordinator.email,
            "password": generate_password_hash(coordinator.password),
            "university": coordinator.university,
            "course": coordinator.course,
            "createdAt": coordinator.createdAt,
            "type": self.type
        })

        return True

    def getAllCoordinators(self):
        coordinators = db.coordinators.find({})

        return coordinators

    def getCoordinatorByCode(self, code):
        coordinator = db.coordinators.find_one({"code": code})

        return coordinator
