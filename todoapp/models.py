from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)