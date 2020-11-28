from django.db import models
from django.db.models.fields import related

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return f"name: {self.name}, address: {self.address}, phone: {self.phone}"

class Product(models.Model):
    name =models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return f"product name: {self.name}, price: {self.price}, quantity: {self.quantity}"
class Order(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete = models.CASCADE,related_name="ordered")
    product = models.ManyToManyField(Product)
    def __str__(self):
        return f"order name: {self.name}, client: {self.client}"
    
