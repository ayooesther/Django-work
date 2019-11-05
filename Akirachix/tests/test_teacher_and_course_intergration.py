import datetime
from django test import Testcase
from student.models import teacher
from course.models import course

class TeacherCourseTestcase(Testcase):
    def setup(self):
        self.teacher_a = Teacher.objects.create(
           first_name = "Esther",
           last_name = "Ayoo",
           gender = "Female",
           email = 'esthherayoo4@gmail.com',
           phone_number = '254701038967',
           date_employed = datetime.date.today(),
        )
        self.teacher_b =Teacher.objects.create(
             "first_name": "Esther",
             "last_name": "Ayoo",
             "gender": "Female",
             "email" : "estherayoo4@gmail.com",
             "phone_number" :'254701038967',
             "date_employed" : datetime.date.today(),
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
    def test_taecher_com_join_a_course(self):
        self.teachera_courses.add(self.python)
        self.assertEqual(self.teacher_a_courses.count(,1))
        self.teacher_a.courses.add(self.javascript)
        self.assertEqual(self.teacher)