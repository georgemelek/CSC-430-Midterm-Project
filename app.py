from flask import Flask, jsonify, request
from flask_cors import CORS

from service import StudentService, ClassService
from models.schema import Schema

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World"

# requires: username, password, first_name, last_name
# optional: address, phone_number, email
# returns: {'status' , 'jwt' : ENCODED({username, password, first_name, last_name, address, phone_number, email})}
@app.route('/student/create', methods=["POST"])
def create_student():
    return jsonify(StudentService().create(request.get_json()))

# requires: username, password
# returns: {'status': 'complete' OR 'incomplete' , 'jwt' : ENCODED({username, password, first_name, last_name, address, phone_number, email}) OR ''}
@app.route('/student/login', methods=["POST"])
def login_student():
    return jsonify(StudentService().login(request.get_json()))

# requires: student_id, class_id
# returns: [{'class_id', 'class_title', 'class_description'}, ...]
@app.route('/student/addclass', methods=["POST"])
def add_class_to_student_schedule():
    return jsonify(StudentService().add_class(request.get_json()))

# requires: username OR id <- neither are mutable
# optional: first_name, last_name, address, phone_number, email
# returns: {'status': 'complete' OR 'incomplete' , 'jwt' : ENCODED({username, password, first_name, last_name, address, phone_number, email}) OR ''}
@app.route('/student/updateinfo', methods=["POST"])
def update_student_info():
    return jsonify(StudentService().update_info(request.get_json()))

# requires: student id in route param
# returns: [{'class_id', 'class_title', 'class_description'}, ...]
@app.route('/student/getclasses/<sid>', methods=["GET"])
def get_student_classes(sid):
    return jsonify(StudentService().get_classes({'student_id' : sid}))

# optional: title, description
# returns : {'id', 'title', 'description', 'created_on'}
@app.route('/class/create', methods=["POST"])
def create_class():
    return jsonify(ClassService().create(request.get_json()))

# returns : [{'id', 'title', 'description', 'created_on'}, ...]
@app.route('/class/getall', methods=["GET"])
def get_all_classes():
    return jsonify(ClassService().get_all())

# requires: class id route param
# returns : {'id', 'title', 'description', 'created_on'}
@app.route('/class/<cid>', methods=["GET"])
def get_class(cid):
    return jsonify(ClassService().get_class({'id': str(cid)}))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)