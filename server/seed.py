from faker import Faker
from app import app
from models import db, Student, Books

fake = Faker()

print("start seeding database.....")
def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        for _ in range(10):
            student = Student(name=fake.name(), email=fake.email())
            db.session.add(student)
            db.session.commit()
        for _ in range(10):
                book = Books(title=fake.sentence(), author=fake.name(), description=fake.sentence(), student_id=fake.random_int(min=1, max=10))
                db.session.add(book)
                db.session.commit()
    
print("seeding database.....")
seed_database()
print("seeding done.....")