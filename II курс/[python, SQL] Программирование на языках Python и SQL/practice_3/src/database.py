from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from src.models import Base, University, Student, Subject, ExamMark, ActivityLecturer, SubjectLecturer
from src.utils import SingletonMeta

from datetime import datetime

DATABASE = "sqlite"
DB_NAME = "university_life.db"


class DataBase(metaclass=SingletonMeta):

    def __init__(self):
        self.engine = create_engine(f"{DATABASE}:///{DB_NAME}")
        self.session: Session = sessionmaker(bind=self.engine)()

    def _create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def _remove_all_tables(self):
        Base.metadata.drop_all(self.engine)

    def select_university(self, **kwargs):
        return self.session.query(University).filter_by(**kwargs).all()

    def create_university(self, id_: int = None, name: str = None, rating: int = None, city: str = None):
        self._create(University, id=id_, name=name, rating=rating, city=city)

    def update_university(self, id_: int, name: str = None, rating: int = None, city: str = None):
        updatable = {
            University.name: name,
            University.rating: rating,
            University.city: city
        }
        self._update(University, id_, updatable)

    def delete_university(self, id_: int):
        self.session.query(University).filter_by(id=id_).delete()

    def select_student(self, **kwargs):
        return self.session.query(Student).filter_by(**kwargs).all()

    def create_student(self, id_: int = None, first_name: str = None, last_name: str = None, stipend: float = None,
                       course: int = None, city: str = None, birthdate: datetime = None, university_id: int = None):
        self._create(Student, id=id_, first_name=first_name, last_name=last_name, stipend=stipend,
                     course=course, city=city, birthdate=birthdate, university_id=university_id)

    def update_student(self, id_: int, first_name: str = None, last_name: str = None, stipend: float = None,
                       course: int = None, city: str = None, birthdate: datetime = None, university_id: int = None):
        updatable = {
            Student.first_name: first_name,
            Student.last_name: last_name,
            Student.stipend: stipend,
            Student.course: course,
            Student.city: city,
            Student.birthdate: birthdate,
            Student.university_id: university_id,
        }
        self._update(Student, id_, updatable)

    def delete_student(self, id_: int):
        self.session.query(Student).filter_by(id=id_).delete()

    def select_subject(self, **kwargs):
        return self.session.query(Subject).filter_by(**kwargs).all()

    def create_subject(self, id_: int = None, name: str = None, hour: int = None, semester: int = None):
        self._create(Subject, id=id_, name=name, hour=hour, semester=semester)

    def update_subject(self, id_: int, name: str = None, hour: int = None, semester: int = None):
        updatable = {
            Subject.name: name,
            Subject.hour: hour,
            Subject.semester: semester
        }
        self._update(Subject, id_, updatable)

    def delete_subject(self, id_: int):
        self.session.query(Subject).filter_by(id=id_).delete()

    def select_exam_mark(self, **kwargs):
        return self.session.query(ExamMark).filter_by(**kwargs).all()

    def create_exam_mark(self, id_: int = None, student_id: int = None, subject_id: int = None,
                         mark: int = None, date: datetime = None):
        self._create(ExamMark, id=id_, student_id=student_id, subject_id=subject_id, mark=mark, date=date)

    def update_exam_mark(self, id_: int, student_id: int = None, subject_id: int = None,
                         mark: int = None, date: datetime = None):
        updatable = {
            ExamMark.student_id: student_id,
            ExamMark.subject_id: subject_id,
            ExamMark.mark: mark,
            ExamMark.date: date
        }
        self._update(ExamMark, id_, updatable)

    def delete_exam_mark(self, id_: int):
        self.session.query(ExamMark).filter_by(id=id_).delete()

    def select_activity_lecturer(self, **kwargs):
        return self.session.query(ActivityLecturer).filter_by(**kwargs).all()

    def create_activity_lecturer(self, id_: int = None, first_name: str = None, last_name: str = None,
                                 city: str = None, university_id: int = None):
        self._create(ActivityLecturer, id=id_, first_name=first_name,
                     last_name=last_name, city=city, university_id=university_id)

    def update_activity_lecturer(self, id_: int = None, first_name: str = None, last_name: str = None,
                                 city: str = None, university_id: int = None):
        updatable = {
            ActivityLecturer.first_name: first_name,
            ActivityLecturer.last_name: last_name,
            ActivityLecturer.city: city,
            ActivityLecturer.university_id: university_id
        }
        self._update(ActivityLecturer, id_, updatable)

    def delete_activity_lecturer(self, id_: int):
        self.session.query(ActivityLecturer).filter_by(id=id_).delete()

    def select_subject_lecturer(self, **kwargs):
        return self.session.query(SubjectLecturer).filter_by(**kwargs).all()

    def create_subject_lecturer(self, id_: int = None, lecturer_id: int = None, subject_id: int = None):
        self._create(SubjectLecturer, id=id_, lecturer_id=lecturer_id, subject_id=subject_id)

    def update_subject_lecturer(self, id_: int = None, lecturer_id: int = None, subject_id: int = None):
        updatable = {
            SubjectLecturer.lecturer_id: lecturer_id,
            SubjectLecturer.subject_id: subject_id,
        }
        self._update(SubjectLecturer, id_, updatable)

    def delete_subject_lecturer(self, id_: int):
        self.session.query(SubjectLecturer).filter_by(id=id_).delete()

    def _create(self, model, **kwargs):
        obj = model(**kwargs)
        self._save(obj)

    def _save(self, obj):
        self.session.add(obj)
        self.session.commit()

    def _update(self, model, id_, updatable):
        updatable = {k: v for k, v in updatable.items() if v}
        self.session.query(model).filter_by(id=id_).update(updatable)
