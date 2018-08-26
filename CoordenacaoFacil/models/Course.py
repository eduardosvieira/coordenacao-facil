from CoordenacaoFacil import db
from bson.objectid import ObjectId

class Course():
    def __init__(self, id=0, name="", coordinator=None, code=""):
        self.id = id
        self.name = name
        self.code = code
        self.coordinator = coordinator


    def createCourse(self, course=None):
        db.courses.insert({
            "name": course.name,
            "code": course.code,
            "coordinator": course.coordinator
        })

        return True

    def getAllCourses(self):
        courses = db.courses.find({})

        return courses

    def getCourseById(self, course_id):
        course = db.courses.find_one({"_id": ObjectId(course_id)})

        return course
