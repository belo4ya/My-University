from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    CheckConstraint
)
from sqlalchemy.ext.declarative import as_declarative, declared_attr

__all__ = [
    'Base',
    'City',
    'ExamMark',
    'Lecturer',
    'Student',
    'Subject',
    'SubjectLecturer',
    'University'
]

CASCADE = "CASCADE"
SHORT_VARCHAR = 80
MIDDLE_VARCHAR = 255


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(self):
        table_name = ''
        ascii_upper = range(ord('A'), ord('Z') + 1)
        for i, s in enumerate(self.__name__):
            if ord(s) in ascii_upper and i != 0:
                table_name += '_'
            table_name += s.upper()

        return table_name + 'S'

    def __repr__(self):
        field_strings = []
        for attr in self.__repr_attrs__:
            field_strings.append(f'{attr}={getattr(self, attr)}')

        return f"<{self.__class__.__name__} ({', '.join(field_strings)})>"

    __str__ = __repr__
    __repr_attrs__ = ['id']


class City(Base):
    name = Column(String(SHORT_VARCHAR))

    __tablename__ = "CITIES"
    __repr_attrs__ = ['name']


class ExamMark(Base):
    mark = Column(Integer)
    date = Column(DateTime)
    student_id = Column(Integer, ForeignKey("STUDENTS.id", ondelete=CASCADE))
    subject_id = Column(Integer, ForeignKey("SUBJECTS.id", ondelete=CASCADE))

    __repr_attrs__ = ['mark', 'date', 'student_id', 'subject_id']


class Lecturer(Base):
    first_name = Column(String(SHORT_VARCHAR))
    last_name = Column(String(SHORT_VARCHAR))
    city = Column(String(SHORT_VARCHAR))
    university_id = Column(Integer, ForeignKey("UNIVERSITIES.id", ondelete=CASCADE))

    __repr_attrs__ = ['first_name', 'last_name', 'city', 'university_id']


class Student(Base):
    first_name = Column(String(SHORT_VARCHAR))
    last_name = Column(String(SHORT_VARCHAR))
    stipend = Column(Float, CheckConstraint("stipend >= 0.00", name="stipend_is_positive"))
    course = Column(Integer)
    city = Column(String(SHORT_VARCHAR))
    birthdate = Column(DateTime)
    university_id = Column(Integer, ForeignKey("UNIVERSITIES.id", ondelete=CASCADE))

    __repr_attrs__ = ['first_name', 'last_name', 'stipend', 'course', 'city', 'birthdate', 'university_id']


class SubjectLecturer(Base):
    lecturer_id = Column(Integer, ForeignKey("LECTURERS.id", ondelete=CASCADE))
    subject_id = Column(Integer, ForeignKey("SUBJECTS.id", ondelete=CASCADE))

    __tablename__ = "SUBJECTS_LECTURERS"
    __repr_attrs__ = ['lecturer_id', 'subject_id']


class Subject(Base):
    name = Column(String(SHORT_VARCHAR), index=True)
    hour = Column(Integer, index=True)
    semester = Column(Integer)

    __repr_attrs__ = ['name', 'hour', 'semester']


class University(Base):
    name = Column(String(SHORT_VARCHAR))
    rating = Column(Integer)
    city = Column(String(SHORT_VARCHAR))

    __tablename__ = "UNIVERSITIES"
    __repr_attrs__ = ['name', 'rating', 'city']
