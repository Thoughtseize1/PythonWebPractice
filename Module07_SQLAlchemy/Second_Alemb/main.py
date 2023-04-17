from datetime import datetime
from sqlalchemy.orm import joinedload, subqueryload
from sqlalchemy import and_

from src.db import session
from src.models import Student, Teacher, ContactPerson, TeacherStudent


def get_student_old():
    students = session.query(Student).join(Student.teachers).all()
    for st in students:
        print(f"ID - {st.id} Name: {st.first_name} {st.last_name}")
        print(f"{[t.full_name for t in st.teachers]}")


def get_student_with_joinload():
    students = session.query(Student).options(joinedload(Student.teachers), joinedload(Student.contacts)).all()
    for st in students:
        print(f"ID - {st.id} Name: {st.first_name} {st.last_name}")
        print(f"Teacher is: {[t.full_name for t in st.teachers]}")
        print(f"Contacts: {[c.full_name+'. Phone: '+c.phone for c in st.contacts]}")


def get_student_sub():
    students = session.query(Student).options(subqueryload(Student.teachers)).all()
    for st in students:
        print(f"Student's ID - {st.id} Name: {st.first_name} {st.last_name}")
        print(f"{[t.full_name for t in st.teachers]}")


def get_teachers_with_their_students():
    teachers = session.query(Teacher).options(subqueryload(Teacher.students)).all()
    for tc in teachers:
        print(f"ID - {tc.id} TeacherName: {tc.full_name}")
        print("Students:", end="")
        print(f"{[st.full_name for st in tc.students]}")


def get_only_teachers():
    teachers = session.query(Teacher).all()
    for tc in teachers:
        print(f"ID - {tc.id} TeacherName: {tc.full_name}")


def get_students_full():
    students = session.query(Student.id, Student.full_name, Teacher.full_name, ContactPerson.full_name) \
        .select_from(Student).join(TeacherStudent).join(Teacher).join(ContactPerson).all()
    print(students)


def get_students_full_from_teachers_and_students():
    students = session.query(Student.id, Student.full_name, Teacher.full_name, ContactPerson.full_name) \
        .select_from(TeacherStudent).join(Student).all()
    print(students)


if __name__ == "__main__":
    # get_student_sub()
    # get_teachers_with_their_students()
    # get_only_teachers()
    # get_student_with_joinload()
    # get_students_full()
    get_students_full_from_teachers_and_students()
