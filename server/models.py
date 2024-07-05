from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # def __repr__(self):
    #     return f"Student('{self.name}', '{self.email}')"
    
    books = db.relationship("Books", backref='student',lazy=True)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(200),  nullable=False)
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)