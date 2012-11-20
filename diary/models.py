from django.db import models
from diary.validators import *

class Person(models.Model):
    first_name = models.CharField(max_length = 30, validators = [validate_string])
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    city = models.CharField(max_length = 15, null = True,blank = True)
    state = models.CharField(max_length = 15, null = True, blank = True)
    country = models.CharField(max_length = 15, null = True, blank = True)
    pincode = models.CharField(max_length = 10, blank = True, null=True, validators = [validate_number])

class Phone(models.Model):
    person = models.ForeignKey('Person')
    number = models.CharField(max_length=10, validators = [validate_number])
