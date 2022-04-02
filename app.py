from flask import Flask, jsonify, request
from flask_cors import CORS

from service import StudentService
from models import Schema

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/student/create', methods=["POST"])
def create_student():
    return jsonify(StudentService().create(request.get_json()))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)