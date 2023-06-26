import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Jewelry(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='jewelry/')
    size = models.IntegerField()
    large = models.IntegerField()
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Registry(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    confirmPass = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name +" "+ self.surname

class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Payment(models.Model):
    city = models.CharField(max_length=250)
    sum_price = models.IntegerField()
    streedAndNumber = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=250)
    cardNumber = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.city +" "+ self.streedAndNumber