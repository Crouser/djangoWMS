from django.db import models
from django.utils import timezone

class Data(models.Model):
    temperature = models.IntegerField()
    pressure = models.IntegerField()
    dateTime = models.DateTimeField(default=timezone.now)
