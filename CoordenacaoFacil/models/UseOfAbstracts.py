from bson.objectid import ObjectId
from CoordenacaoFacil import db

class UseOfAbstracts():
    def __init__(self, origin=None, destiny=None, student=None, menu=None, createdAt=""):
        self.origin = origin
        self.destiny = destiny
        self.student = student
        self.menu = menu
        self.status = "Processamento"
        self.createdAt = createdAt

    def create(self, uoa=None):
        try:
            db.useOfAbstracts.insert({
                "origin": uoa.origin,
                "destiny": uoa.destiny,
                "student": uoa.student,
                "menu": uoa.menu,
                "status": self.status,
                "createdAt": self.createdAt
            })

            return True
        except:
            print("Problema ao criar aproveitamento de cadeiras.")
            return False

    def getAllUOA(self):
        try:
            uoas = db.useOfAbstracts.find({})

            return uoas
        except:
            print("Houve um problema ao retornar uoas.")
            return None

    def getAllUOAByCourse(self, course=""):
        try:
            uoas = db.useOfAbstracts.find({"student.course.code": course})

            return uoas
        except:
            print("Houve um problema ao retornar uoas.")
            return None

    def getUOAByCode(self, code):
        uoa = db.useOfAbstracts.find_one({"_id": ObjectId(code)})

        return uoa

    def delete(self, id):
        try:
            db.useOfAbstracts.remove({"_id": ObjectId(id)})

            return True
        except:
            print("Houve um problema ao remover UOA.")
            return False
