from src.db import session
from src.models import Student
from src.models import ContactPerson


def delete_all_students():
    session.query(Student).delete()
    session.commit()


def delete_all_contacts():
    session.query(ContactPerson).delete()
    session.commit()


if __name__ == '__main__':
    delete_all_contacts()
