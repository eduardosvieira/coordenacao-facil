from CoordenacaoFacil.models.User import User
from CoordenacaoFacil import db

class Teacher(User):
    def __init__(self, id=0, code=0, name="", email="", password="", type="", createdAt="", course=None, university=None):
        super().__init__(id=id, code=code, name=name, email=email, password=password, type=type, createdAt=createdAt)
        self.course = course
        self.university = university


    def createTeacher(self, teacher=None):
        db.users.insert({
            "name": teacher.name,
            "code": teacher.code,
            "course": teacher.course,
            "type": "teacher"
        })

        return True

    def getAllTeachers(self):
        teachers = db.users.find({})

        return teachers
