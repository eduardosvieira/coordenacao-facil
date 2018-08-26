from CoordenacaoFacil import db

class Abstract():
    def __init__(self, id=0, name="", code="", teacher=None):
        self.id = id
        self.name = name
        self.code = code
        self.teacher = teacher


    def createAbstract(self, abstract=None):
        db.abstracts.insert({
            "name": abstract.name,
            "code": abstract.code,
            "teacher": abstract.teacher,
        })

        return True

    def getAllAbstracts(self):
        abstracts = db.abstracts.find({})

        return abstracts
