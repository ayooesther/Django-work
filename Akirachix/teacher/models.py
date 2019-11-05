from django.db import models



class Teacher(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  gender=models.CharField(max_length=20)
  email=models.EmailField(max_length=70)
  phone_number=models.CharField(max_length=60)
  date_employed=models.DateField(max_length=70)
  id_number=models.IntegerField()
  profession=models.CharField(max_length=20,null=True,)



  def __str__(self):
  	 return self.first_name