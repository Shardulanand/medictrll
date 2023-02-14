from distutils import text_file
from email.policy import default
from django.db import models

class message(models.Model):
    name=models.CharField(max_length=50)
    phone=models.FloatField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    message=models.TextField()
