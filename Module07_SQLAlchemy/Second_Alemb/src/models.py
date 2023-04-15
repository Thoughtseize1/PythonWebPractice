from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
    Date,
    event,
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(125), nullable=False)
    last_name = Column(String(125), nullable=False)
    email = Column(String(30), nullable=False)
    phone = Column(String(25), nullable=False)
    address = Column(String(200), nullable=False)
    start_work = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    students = relationship(
        "Student", secondary="teachers_to_students", back_populates="teachers"
    )

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(125), nullable=False)
    last_name = Column(String(125), nullable=False)
    email = Column(String(30), nullable=False)
    phone = Column(String(25), nullable=False)
    address = Column(String(200), nullable=False)
    start_study = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    teachers = relationship(
        "Teacher", secondary="teachers_to_students", back_populates="students"
    )


class TeacherStudent(Base):
    __tablename__ = "teachers_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(
        "teacher_id", Integer, ForeignKey("teachers.id", ondelete="CASCADE")
    )
    student_id = Column(
        "student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")
    )


@event.listens_for(Teacher, "before_update")
def update_updated_at(mapper, conn, target):
    target.updated_at = func.now()
    print(target.updated_at)


@event.listens_for(Student, "before_update")
def update_updated_at(mapper, conn, target):
    target.updated_at = func.now()
    print(target.updated_at)
