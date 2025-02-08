from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
