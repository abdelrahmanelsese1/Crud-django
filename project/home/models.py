from django.db import models

# Create your models here.



class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=100)



