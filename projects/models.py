from django.db import models

# Create your models here.
class Projects(models.Model):
    name=models.CharField(max_length=200)
    link=models.CharField(max_length=200)

