from django.db import models

# Create your models here.
# models.py


class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.TextField()
