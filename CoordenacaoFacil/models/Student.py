from User import User
from CoordenacaoFacil import db

class Student(User):
    def __init__(self, code="", name="", email="", password="", course=None, createdAt=""):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.course = course
        self.createdAt = createdAt

    def create(self, student=None):
        try:
            db.students.insert({
                "code": student,
                "name": name,
                "email": email,
                "password": password,
                "course": course,
                "createdAt": createdAt
            })

            return True
        except:
            print("Houve um problema ao cadastrar novo estudante.")
            return False
