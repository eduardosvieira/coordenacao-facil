from CoordenacaoFacil import db

class Abstract():
    def __init__(self, code="", name="", createdAt=""):
        self.code = code
        self.name = name
        self.createdAt = createdAt


    def create(self, abstract=None):
        db.abstracts.insert({
            "code": abstract.code,
            "name": abstract.name,
            "createdAt": abstract.createdAt,
        })

        return True

    def getAllAbstracts(self):
        abstracts = db.abstracts.find({})

        return abstracts

    def getAbstractByCode(self, code=""):
        abstract = db.abstracts.find_one({"code": code})

        return abstract
