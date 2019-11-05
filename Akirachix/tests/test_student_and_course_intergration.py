import datetime
from django test import Testcase
from student.models import student
from course.models import course

class StudentCourseTestcase(Testcase):
    def setup(self):
        self.student_a = Student.objects.create(
            first_name = "Esther",
           last_name = "Ayoo",
           date_of_birth = datetime.date(1999,3,30),
           gender = "Female",
           registration_no = "1234",
           email = 'esthherayoo4@gmail.com',
           phone_number = '254701038967',
           date_joined = datetime.date.today(),
        )
        self.student_b =Student.objects.create(
            "first_name": "Esther",
             "last_name": "Ayoo",
             "date_of_birth":  datetime.date(1999,3,30),
             "gender": "Female",
             "registration_no":  "5678",
             "email" : "estherayoo4@gmail.com",
             "phone_number" :'254701038967',
             "date_joined" : datetime.date.today(),
        )
        self.python = Course.objects.create(
            name="python",
            duration_months=datetime.date.today(),
            start_date=datetime.date.today()
            end_date=datetime.date.today(),
            description="Python courses",
            
        )
        self.javascript=Course.objects.create(
            name="javascript",
            duration_months=datetime.date.today(),
            start_date=datetime.date.today()
            end_date=datetime.date.today(),
            description="javascript courses",

        )
        self.kotlin = Course.objects.create(
            name="python",
            duration_months=datetime.date.today(),
            start_date=datetime.date.today()
            end_date=datetime.date.today(),
            description="kotlin courses",
        )
    def test_student_com_join_a_course(self):
        self.studenta_courses.add(self.python)
        self.assertEqual(self.student_a_courses.count(,1))
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student)