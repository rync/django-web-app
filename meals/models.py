from django.db import models

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_time = models.IntegerField()  # in minutes

class Household(models.Model):
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField(Meal, related_name='households')

