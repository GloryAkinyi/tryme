from django.db import models


# Create your models here.
# Define a model in your Django application to represent
# the data you want to store in the database
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname + " " + self.lastname
