from django.db import models
from course.models import Course


class Student(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  date_of_birth=models.DateField()
  gender=models.CharField(max_length=20)
  registration=models.CharField(max_length=10)
  email=models.EmailField(max_length=70)
  phone_number=models.CharField(max_length=60)
  date_joined=models.DateField(max_length=70)
  courses=models.ManyToManyField(Course null=True,blank=True, related_name="students")
  profile=models.ImageField(upload_to="profile_image",blank=True)


  def __str__(self):
        return self.first_name


  
  


