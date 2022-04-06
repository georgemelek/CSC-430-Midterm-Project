from flask import Flask, jsonify, request
from flask_cors import CORS

from service import StudentService, ClassService
from models.schema import Schema

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/student/create', methods=["POST"])
def create_student():
    return jsonify(StudentService().create(request.get_json()))

@app.route('/student/login', methods=["POST"])
def login_student():
    return jsonify(StudentService().login(request.get_json()))

@app.route('/class/create', methods=["POST"])
def create_class():
    return jsonify(ClassService().create(request.get_json()))

@app.route('/class/getall', methods=["GET"])
def get_all_classes():
    return jsonify(ClassService().get_all())

@app.route('/class/<cid>', methods=["GET"])
def get_class(cid):
    return jsonify(ClassService().get_class({'id': str(cid)}))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)