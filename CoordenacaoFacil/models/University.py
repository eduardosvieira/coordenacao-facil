from CoordenacaoFacil import db
from bson.objectid import ObjectId

class University():
    def __init__(self, id=0, name="", code=""):
        self.id = id
        self.name = name
        self.code = code


    def createUniversity(self, university=None):
        db.universities.insert({
            "name": university.name,
            "code": university.code
        })

        return True

    def getAllUniversities(self):
        universities = db.universities.find({})

        return universities

    def getUniversityByCode(self, code):
        university = db.universities.find_one({"code": code})

        return university
