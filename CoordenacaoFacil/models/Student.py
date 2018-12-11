from werkzeug.security import generate_password_hash, check_password_hash

from CoordenacaoFacil import db

class Student():
    def __init__(self, code="", name="", email="", password="", course=None, university=None, createdAt=""):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.university = university
        self.course = course
        self.createdAt = createdAt

    def create(self, student=None):
        try:
            db.students.insert({
                "code": student.code,
                "name": student.name,
                "email": student.email,
                "password": generate_password_hash(student.password),
                "university": student.university,
                "course": student.course,
                "createdAt": student.createdAt
            })

            return True
        except:
            print("Houve um problema ao cadastrar novo estudante.")
            return False
