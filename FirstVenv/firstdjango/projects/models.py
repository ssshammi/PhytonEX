from django.db import models

# Create your models here.
class Project(models.Model):
    title   = models.TextField()
    desc    = models.TextField()
    date    = models.TextField()