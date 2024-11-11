from django.db import models


class Badge(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.uid

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    badge = models.OneToOneField(Badge, on_delete=models.CASCADE, related_name='teacher')
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')
    def __str__(self):
        return self.name
