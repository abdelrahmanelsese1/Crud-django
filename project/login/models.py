from django.db import models

# Create your models here.
class SignupInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)






