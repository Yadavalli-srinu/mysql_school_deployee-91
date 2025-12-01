from django.db import models

class student_model(models.Model):
    name=models.CharField(max_length=50)
    pin=models.IntegerField()
