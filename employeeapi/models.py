from django.db import models

# Create your models here.
class employee(models.Model):
    username = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField()

