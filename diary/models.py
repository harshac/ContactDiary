from django.db import models
from diary.validators import *

class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True, validators = [validate_string])
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=15, null=True)
    state = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=15, null=True)
    pin_code = models.CharField(max_length=10, null=True, validators = [validate_number])

class Phone(models.Model):
    person = models.ForeignKey('Person')
    number = models.CharField(max_length=10, validators = [validate_number])
