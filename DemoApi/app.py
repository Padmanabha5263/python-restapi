from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self,name):
        return jsonify({"student-name": name})

api.add_resource(Student, "/student/<string:name>")        #http://127.0.0.1:5000/student/padmanabha
app.run(port=5000)
