from django.db import models

class Relative(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    age = models.IntegerField()
    birth_date = models.DateField()

