from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    # phone_no = PhoneField(blank=True, help_text='Contact phone number')

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=400,null=True)

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()