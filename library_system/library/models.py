from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)


class Member(models.Model):
    name = models.CharField(max_length=100)
    joined_date = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='members')


class LibraryCard(models.Model):
    card_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateField()
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='library_card')


class Book(models.Model):
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(Member, related_name='books')




