from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 100)
    phone = models.IntegerField()
    passWord = models.CharField(max_length=50)
    def __str__(self):
        return (f"{self.name} {self.email} {self.phone} {self.passWord}")