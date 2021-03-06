from werkzeug.security import generate_password_hash, check_password_hash

from CoordenacaoFacil import db

class Teacher():
    def __init__(self, code="", name="", email="", password="", createdAt="", course=None, university=None):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.university = university
        self.course = course
        self.createdAt = createdAt
        self.type = "teacher"


    def create(self, teacher=None):
        db.teachers.insert({
            "code": teacher.code,
            "name": teacher.name,
            "email": teacher.email,
            "password": teacher.password,
            "university": teacher.university,
            "course": teacher.course,
            "createdAt": teacher.createdAt,
            "type": self.type
        })

        return True

    def getAllTeachers(self):
        teachers = db.teachers.find({})

        return teachers

    def getAllTeachersByCourse(self, course=""):
        teachers = db.teachers.find({"course.code": course})

        return teachers

    def getTeacherByCode(self, code):
        teacher = db.teachers.find_one({"code": code})

        return teacher
