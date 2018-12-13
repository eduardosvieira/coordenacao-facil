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
