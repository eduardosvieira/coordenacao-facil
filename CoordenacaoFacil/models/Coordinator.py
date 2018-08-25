from User import User

class Coordinator(User):
    def __init__(self, id=0, code=0, name="", email="", password="", type="", createdAt="", course=None, university=None):
        super.__init__(id=0, code=0, name="", email="", password="", type="", createdAt="")
        self.course = course
        self.university = university
