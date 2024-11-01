from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    views = models.TextField(default=0)
    is_published = models.BooleanField(default=False)
    