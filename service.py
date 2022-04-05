from models import StudentModel
from secret import SECRET_KEY
import jwt

class StudentService:
    def __init__(self):
        self.model = StudentModel()

    def create(self, params):
        return self.model.create(params)
    
    def login(self, params):
        isValid = self.model.login(params)
        response = {"status": "complete" if isValid else "incomplete", "jwt" : ""}
        if isValid:
            student_info = self.model._get_info({'username' : params['username']})
            response['jwt'] = jwt.encode(student_info, SECRET_KEY, algorithm="HS256")
        
        return response