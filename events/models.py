from django.db import models
from main.models import Club


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    date = models.DateTimeField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)


class GeneralEvent(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    date = models.DateTimeField()
    published = models.BooleanField(default=True)
