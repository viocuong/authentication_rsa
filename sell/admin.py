from sell.models import Client, Order, Product
from django.contrib import admin
from django.db import models
from . import models


# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
