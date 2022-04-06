import jwt
from models.student import StudentModel
from models.class_model import ClassModel
from secret import SECRET_KEY

class StudentService:
    def __init__(self):
        self.model = StudentModel()

    def create(self, params):
        return self.model.create(params)
    
    def login(self, params):
        isValid = self.model.login(params)
        response = {"status": "incomplete", "jwt" : ""}
        if isValid:
            student_data = self.model.get_student({'username' : params['username']})
            response['jwt'] = jwt.encode(student_data, SECRET_KEY, algorithm="HS256")
            response['status'] = 'complete'

        return response

class ClassService:
    def __init__(self):
        self.model = ClassModel()

    def create(self, params):
        return self.model.create(params)

    def get_class(self, params):
        return self.model.get_class(params)

    def get_all(self):
        return self.model.get_all_classes()