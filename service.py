from models import StudentModel

class StudentService:
    def __init__(self):
        self.model = StudentModel()

    def create(self, params):
        return self.model.create(params)
    