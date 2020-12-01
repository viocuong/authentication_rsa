from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length = 200, default= "")
    publicKey = models.CharField(max_length = 200, default="")
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 100)
    phone = models.IntegerField()
    
    def __str__(self):
        return (f"{self.name} {self.email} {self.phone} {self.userId} {self.publicKey}")