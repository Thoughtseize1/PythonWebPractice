from faker import Faker
from src.db import session
from src.models import Student

fake = Faker("uk_UA")


def create_students():
    for _ in range(2):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_study=fake.date_between(start_date="-5y"),
        )
        session.add(student)
    session.commit()


if __name__ == "__main__":
    create_students()
