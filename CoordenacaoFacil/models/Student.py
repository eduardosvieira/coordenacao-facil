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
        self.type = "student"

    def create(self, student=None):
        try:
            db.students.insert({
                "code": student.code,
                "name": student.name,
                "email": student.email,
                "password": generate_password_hash(student.password),
                "university": student.university,
                "course": student.course,
                "createdAt": student.createdAt,
                "type": self.type
            })

            return True
        except:
            print("Houve um problema ao cadastrar novo estudante.")
            return False


    def login(self, code="", password=""):
        try:
            student = db.students.find_one({
                "code": code
            })

            if student:
                if check_password_hash(student["password"], password):
                    return True
            return False
        except:
            print("Houve um problema ao entrar na aplicação.")
            return False

    def getUserByCode(self, code=""):
        try:
            student = db.students.find_one({
                "code": code
            })

            return student
        except:
            print("Houve um problema ao obter estudante.")
            return False
