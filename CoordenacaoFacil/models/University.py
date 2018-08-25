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

    def getAllUniversities(self, university_id=0):
        universities = db.universities.find({"_id": ObjectId(university_id)})

        return universities

    def getUniversityById(self, university_id=0):
        university = db.universities.find_one({"_id": ObjectId(university_id)})

        return university
