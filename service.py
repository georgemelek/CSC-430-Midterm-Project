import jwt
from models.student import StudentModel
from models.class_model import ClassModel
from secret import SECRET_KEY

class StudentService:
    def __init__(self):
        self.model = StudentModel()

    def _student_info_payload(self, params):
        response = {"status": "incomplete", "jwt" : ""}
        if params['valid']:
            student_data = self.model.get_student({'username' : params.get('username', ''), 'id' : params.get('id', '')})
            response['jwt'] = jwt.encode(student_data, SECRET_KEY, algorithm="HS256")
            response['status'] = 'complete'

        return response

    def create(self, params):
        data = self.model.create(params)
        data['valid'] = True

        return self._student_info_payload(data)

    def login(self, params):
        params['valid'] = self.model.login(params)

        return self._student_info_payload(params)

    def update_info(self, params):
        params['valid'] = self.model.update_info(params)
        
        return self._student_info_payload(params)

    def add_class(self, params):
        return self.model.add_class(params)

    def get_classes(self, params):
        return self.model.get_classes(params)

class ClassService:
    def __init__(self):
        self.model = ClassModel()

    def create(self, params):
        return self.model.create(params)

    def get_class(self, params):
        return self.model.get_class(params)

    def get_all(self):
        return self.model.get_all_classes()