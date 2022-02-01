from django.db import models

# Create your models here.
class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    track = models.CharField(max_length=200)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

