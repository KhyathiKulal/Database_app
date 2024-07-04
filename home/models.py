from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    classes = models.CharField(max_length=10)
    regcode = models.TextField()


    def __str__(self):  #name will change to the name filled in the form
        return self.name
    

