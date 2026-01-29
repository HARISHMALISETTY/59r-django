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

class Resolutions(models.Model):
    person_name=models.CharField(max_length=100)
    resolution=models.CharField(max_length=100)
    Deadline_in_mnths=models.IntegerField()
    lastYearResolutionSatus=models.CharField(max_length=150)
    lastYearAchievements=models.CharField(max_length=250)

class UserDetails(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=150)
    userEmail=models.EmailField(unique=True)

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role=models.CharField(max_length=250,default="user")