from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    
