from django.db import models

# Create your models here.
class Students(models.Model):
    stud_name=models.CharField(max_length=100)
    stud_age=models.IntegerField()
    stud_gender=models.CharField(max_length=100)
    stud_email=models.EmailField(unique=True)

class Employees(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_age=models.IntegerField()
    emp_gender=models.CharField(max_length=100)
    emp_email=models.EmailField(unique=True)

