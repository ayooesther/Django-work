from django.db import models
from teacher.models import Teacher


class Course(models.Model):
	name=models.CharField(max_length=50)
	duration_months=models.IntegerField()
	start_date=models.DateField(max_length=10)
	end_date=models.DateField(max_length=10)
	description=models.TextField(max_length=100)
	teacher=models.ForeignKey(Teacher,null=True, on_delete=models.CASCADE)


	def __str__(self):
		return self.name



