from CoordenacaoFacil import db
from bson.objectid import ObjectId

class Course():
    def __init__(self, code="", name="", createdAt="", coordinator=None, university=None):
        self.id = id
        self.name = name
        self.code = code
        self.coordinator = coordinator
        self.university = university
        self.createdAt = createdAt


    def createCourse(self, course=None):
        db.courses.insert({
            "name": course.name,
            "code": course.code,
            "coordinator": course.coordinator,
            "university": course.university,
            "createdAt": course.createdAt
        })

        return True

    def getAllCourses(self):
        courses = db.courses.find({})

        return courses

    def getCourseByCode(self, code):
        course = db.courses.find_one({"code": code})

        return course
