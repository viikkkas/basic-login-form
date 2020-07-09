from django.db import models

# Create your models here.
class Intro(models.Model):
    name = models.CharField(max_length=15)
    uni = models.CharField(max_length=100)
    school1 = models.CharField(max_length=100)
    school2 = models.CharField(max_length=100)