from datetime import datetime
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class AddCourses(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    # image = models.ImageField(upload_to="cimg", default=None)
    # date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course

class AddStudents(models.Model):
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    smobile = models.IntegerField()
    saddress= models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    # addcourse= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
    scourse= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
    # sduration= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
    # sfees= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
    # simage = models.ImageField(upload_to="simg", default=None)
    
    def __str__(self):
        return self.sname

