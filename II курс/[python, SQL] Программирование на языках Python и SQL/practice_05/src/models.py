from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, CheckConstraint, Float)

__all__ = [
    "University",
    "Student",
    "Subject",
    "ExamMark",
    "ActivityLecturer",
    "SubjectLecturer"
]

CASCADE = "CASCADE"
SHORT_VARCHAR = 80


@as_declarative()
class Base(object):
    id = Column(Integer(), primary_key=True, autoincrement=True)

    @classmethod
    @property
    def columns(cls):
        return cls.__table__.columns

    c = columns

    def _repr(self, **args) -> str:
        field_strings = []
        for key, field in args.items():
            field_strings.append(f'{key}={field!r}')

        return f"<{self.__class__.__name__} {field_strings}>"

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    def __repr__(self) -> str:
        return self._repr(id=self.id)

    __str__ = __repr__


class University(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)
    rating = Column(Integer())
    city = Column(String(SHORT_VARCHAR), nullable=False)

    def __repr__(self):
        return self._repr(name=self.name, rating=self.rating, city=self.city)


class Student(Base):
    first_name = Column(String(SHORT_VARCHAR), nullable=False)
    last_name = Column(String(SHORT_VARCHAR), nullable=False)
    stipend = Column(Float(), CheckConstraint("stipend >= 0.00", name="stipend_is_positive"))
    course = Column(Integer(), nullable=False)
    city = Column(String(SHORT_VARCHAR))
    birthdate = Column(DateTime())
    university_id = Column(Integer(), ForeignKey("university.id", ondelete=CASCADE))

    def __repr__(self):
        return self._repr(first_name=self.first_name,
                          last_name=self.last_name,
                          stipend=self.stipend,
                          course=self.course,
                          birthdate=self.birthdate,
                          university_id=self.university_id)


class Subject(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)
    hour = Column(Integer(), nullable=False)
    semester = Column(Integer(), nullable=False)

    def __repr__(self):
        return self._repr(name=self.name, hour=self.hour, semester=self.semester)


class ExamMark(Base):
    student_id = Column(Integer(), ForeignKey("student.id", ondelete=CASCADE))
    subject_id = Column(Integer(), ForeignKey("subject.id", ondelete=CASCADE))
    mark = Column(Integer())
    date = Column(DateTime(), nullable=False)

    def __repr__(self):
        return self._repr(student_id=self.student_id,
                          subject_id=self.subject_id,
                          mark=self.mark,
                          date=self.date)


class ActivityLecturer(Base):
    first_name = Column(String(SHORT_VARCHAR), nullable=False)
    last_name = Column(String(SHORT_VARCHAR), nullable=False)
    city = Column(String(SHORT_VARCHAR))
    university_id = Column(Integer(), ForeignKey("university.id", ondelete=CASCADE))

    def __repr__(self):
        return self._repr(first_name=self.first_name,
                          last_name=self.last_name,
                          city=self.city,
                          university_id=self.university_id)


class SubjectLecturer(Base):
    lecturer_id = Column(Integer(), ForeignKey("activitylecturer.id", ondelete=CASCADE))
    subject_id = Column(Integer, ForeignKey("subject.id", ondelete=CASCADE))

    def __repr__(self):
        return self._repr(lecturer_id=self.lecturer_id, subject_id=self.subject_id)
