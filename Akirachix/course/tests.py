from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Course
from student.forms import CourseForm
import datetime
from django.test import Client
from django.urls import reverse
class StudentTestCase(TestCase):
   def setUp(self):
       self.course = Course(
           first_name = "Esther",
           last_name = "Ayoo",
           date_of_birth = datetime.date(1999,3,30),
           gender = "Female",
           registration_no = "1234",
           email = 'esthherayoo4@gmail.com',
           phone_number = '254701038967',
           date_joined = datetime.date.today(),
           )
   def test_full_name_contains_first_name(self):
       self.assertIn(self.student.first_name, self.student.full_name())
   def test_full_name_contains_last_name(self):
       self.assertIn(self.student.first_name, self.student.full_name())
   def test_age_always_above_17(self):
       self.assertFalse(self.student.clean() < 17)
   def test_age_always_above_30(self):
       self.assertFalse(self.student.clean() >  30)
class AddStudentTestCase(TestCase):
   def setUp(self):
       self.data = {"name":
                    }
       self.bad_data = {"first_name": "Esther",
                        "last_name": "Ayoo",
                        "date_of_birth": datetime.date(1999,3,30),
                        "gender": "Female",
                        "registration_no":  "5678",
                        "email" : 'ayooesther',
                        "phone_number" :'254701038967',
                        "date_joined" : datetime.date.today(),
                   }
   def test_student_form_accepts_valid_data(self):
       form = StudentForm(self.data)
       self.assertFalse(form.is_valid())
   def test_student_from_rejects_invalid_data(self):
       form = StudentForm(self.bad_data)
       self.assertFalse(form.is_valid())
   def test_add_student_view(self):
       client = Client()
       url = reverse ("add_student")
       response = client.post(url,self.data)
       self.assertTrue(response.status_code,200)
   def test_add_student_view_invalid_data(self):
       client = Client()
       url = reverse ("add_student")
       response = client.post(url,self.bad_data)
       self.assertEqual(response.status_code,400)