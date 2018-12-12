from CoordenacaoFacil import db

class Abstract():
    def __init__(self, code="", name="", createAt=""):
        self.code = code
        self.name = name
        self.createAt = createAt


    def createAbstract(self, abstract=None):
        db.abstracts.insert({
            "code": abstract.code,
            "name": abstract.name,
            "createAt": abstract.createAt,
        })

        return True

    def getAllAbstracts(self):
        abstracts = db.abstracts.find({})

        return abstracts
