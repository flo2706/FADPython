from person import Person
import random

class Student(Person):
    def __init__(self, lastname, firstname, address) -> None:
        super().__init__(lastname, firstname, address)
        self.student_id = self.generate_student_id(lastname, firstname)
        self.courses = []

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def add_course(self, course):
        self.__courses.append(course.strip())

    def generate_student_id(self, lastname, firstname):
        firstname_letters = firstname[:2].upper()
        lastname_letters = lastname[:2].upper()
        numbers = str(random.randint(1000, 9999))
        student_id = firstname_letters + lastname_letters + numbers
        return student_id
    
    def __str__(self) -> str:
        return super().__str__() + f", StudentId: {self.student_id}, Course.s: {self.courses}"
