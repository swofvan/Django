from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length=50)
    percentage = models.CharField(max_length=50)
    result = models.CharField(max_length=50)