from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(max_length=110)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')






