from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 15)
    country = models.CharField(max_length = 15)
    pincode = models.CharField(max_length = 10)


class Phone(models.Model):
    person = models.ForeignKey('Person')
    number = models.CharField(max_length = 10)
