from django.db import models

# Create your models here.
class User(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
