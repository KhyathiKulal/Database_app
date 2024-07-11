from django.db import models
from home.models import Student

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField()
    course_code = models.CharField(max_length=100)
    course_credits = models.IntegerField()
    course_fees = models.IntegerField()

    def __str__(self):  #name will change to the name filled in the form
        return self.course_name
    
class Project(models.Model):
    student_name = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    project_language = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self): 
        return self.project_title