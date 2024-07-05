from flask import Flask, request, jsonify
from  flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
from models import db , Student, Books
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/v1/students", methods=["GET"])
def fetch_students():
    students = Student.query.all()
    students_list = []
    for student in students:
        students_list.append({
            "id": student.id,
            "name": student.name,
            "email": student.email,
        })
    print(students)
    return jsonify(students_list),200
    
@app.route("/v1/students/<int:id>", methods=["GET"])
def fetch_student(id):
    student = Student.query.get_or_404 (id)
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email,
    }),200

@app.route("/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], email=data["email"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({
        "sucess":"student created succsessfully"
    }),201
    
@app.route("/v1/students/<int:id>", methods=["PUT"])
def update_student(id): 
    student = Student.query.get_or_404(id)   
    data = request.get_json()
    
    student.name = data["name"]
    student.email= data["email"]    
    
    db.session.commit()
    return jsonify({
        "sucess":"student updated succsessfully"
    })
    
@app.route("/v1/students/<int:id>", methods=["DELETE"])
def delete_student(id):   
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({
        "sucess":"student deleted succsessfully"
    }), 204
    
if __name__ == '__main__':
    app.run(debug=True)