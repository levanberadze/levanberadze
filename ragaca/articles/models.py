from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=10)
    views = models.PositiveIntegerField()
    is_published = models.BooleanField()
    create_date = models.DateTimeField()